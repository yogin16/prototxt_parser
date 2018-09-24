import sys

from prototxt_parser.prototxt import parse, serialize

if __name__ == '__main__':
    f = open(sys.argv[1])
    dict = parse(f.read())
    print(repr(dict))

    text = serialize(dict, pretty=True)
    print(text)
    assert parse(text) == dict
