import sys

from src.prototxt import parse

if __name__ == '__main__':
    f = open(sys.argv[1])
    print(repr(parse(f.read())))
