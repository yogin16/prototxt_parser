import sys

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
    col = yield optional_colon
    res = None
    if col is not None:
        yield lbrace
        res = yield exp
        yield rbrace
    return key, res


exp = (object_pair | message).many().sep_by(comma).map(tuples_to_dict)


def parse(inp):
    return exp.parse(inp)
