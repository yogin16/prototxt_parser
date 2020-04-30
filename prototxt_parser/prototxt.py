from parsy import generate, regex, string


# Convert an array of tuples array [[(a,b),(a,c)]] to an object {a: [b,c]}
def tuples_to_dict(a):
    # print(a)
    new_dict = {}
    for tuples in a:
        for item in tuples:
            if item[0] not in new_dict:
                new_dict[item[0]] = item[1]
            else:
                merged = new_dict[item[0]]
                if type(merged) is not list:
                    merged = [new_dict[item[0]]]
                merged.append(item[1])
                new_dict[item[0]] = merged
    return new_dict


whitespace = regex(r'\s*')
lexeme = lambda p: p << whitespace
lbrace = lexeme(string('{'))
rbrace = lexeme(string('}'))
colon = lexeme(string(':'))
comma = lexeme(string(','))
true = lexeme(string('true')).result(True)
false = lexeme(string('false')).result(False)
null = lexeme(string('null')).result(None)
number = lexeme(
    regex(r'-?(0|[1-9][0-9]*)([.][0-9]+)?([eE][+-]?[0-9]+)?')
).map(float)
string_part = regex(r'[^"\\]+')
string_esc = string('\\') >> (
        string('\\')
        | string('/')
        | string('"')
        | string('b').result('\b')
        | string('f').result('\f')
        | string('n').result('\n')
        | string('r').result('\r')
        | string('t').result('\t')
        | regex(r'u[0-9a-fA-F]{4}').map(lambda s: chr(int(s[1:], 16)))
)
quoted = lexeme(string('"') >> (string_part | string_esc).many().concat() << string('"'))
identifier = lexeme(regex(r'[a-zA-Z_-][a-zA-Z0-9_+-]*'))
value = quoted | number | identifier | true | false | null
optional_colon = colon.optional()


@generate
def object_pair():
    key = yield identifier
    yield colon
    val = yield value
    return key, val


@generate
def message():
    key = yield identifier
    yield optional_colon
    yield lbrace
    res = yield exp
    yield rbrace
    return key, res


exp = (object_pair | message).many().sep_by(comma).map(tuples_to_dict)


def parse(inp):
    return exp.parse(inp)


def serialize(input_dict, pretty=False):
    if not input_dict:
        return None
    col = ':'

    sb = []
    for key, value in input_dict.items():
        sb.append(key)
        sb.append(col)
        sb.append(prototxt_block(key, value, pretty=pretty))
        if pretty:
            _append_tabs(sb)
    return ''.join(sb)


def prototxt_block(key, ob, tabs=0, pretty=False):
    if ob is None:
        return "null"
    if type(ob) in [str, int, float, bool]:
        return "\"" + str(ob) + "\""
    if type(ob) is list:
        col = ':'
        com = ','
        first = True

        sbuilder = []
        for val in ob:
            if not first:
                sbuilder.append(com)
            if pretty:
                _append_tabs(sbuilder, tabs)
            sbuilder.append(key)
            sbuilder.append(col)
            sbuilder.append(prototxt_block(key, val, tabs + 1, pretty))
            first = False
        return ''.join(sbuilder)
    if type(ob) is dict:
        lbr = '{'
        rbr = '}'
        col = ':'
        com = ','
        space = ' '
        first = True

        sbuilder = [space, lbr]
        for key, val in ob.items():
            if not first:
                sbuilder.append(com)
            if type(val) is not list:
                if pretty:
                    _append_tabs(sbuilder, tabs)
                sbuilder.append(key)
                sbuilder.append(col)
            sbuilder.append(prototxt_block(key, val, tabs + 1, pretty))
            first = False
        if pretty:
            _append_tabs(sbuilder, tabs - 1)
        sbuilder.append(rbr)
        return ''.join(sbuilder)
    raise Exception("Unhandled type: " + type(ob))


def _append_tabs(builder, tabs=0):
    builder.append('\n')
    for x in range(tabs):
        builder.append('\t')
