# prototxt-parser

prototxt-parser allows to parse `*.prototxt` files to python dict objects

## Usage:

From command line from this repo:

```commandline
$ python3 prototxt_parser_main.py prototxt_file
```

Alternatively can use pip as well to get the package:

```commandline
pip3 install --extra-index-url https://testpypi.python.org/pypi prototxt-parser
```

To run, from python:

```python
input_string = ... # the prototxt string to be parsed e.g., open("some_prototxt_file").read()
from prototxt_parser.prototxt import parse
parsed_dict = parse(input_string)
```

