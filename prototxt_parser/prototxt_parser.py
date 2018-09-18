import sys

from prototxt_parser.prototxt import parse

if __name__ == '__main__':
    f = open(sys.argv[1])
    print(repr(parse(f.read())))
