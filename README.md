# prototxt-parser

prototxt-parser allows to parse `*.prototxt` files to python dict objects

Tool using Python's parsy to define parse the serialized prototxt objects' grammar to python dict!

## Usage:

Use pip to get the package:

```commandline
pip3 install prototxt-parser
```

To run, from python, for converting prototxt to python dict:

```python
input_string = ... # the prototxt string to be parsed e.g., open("some_prototxt_file").read()

from prototxt_parser.prototxt import parse
parsed_dict = parse(input_string)
```

To generate prototxt, from python dict:

```python
from prototxt_parser.prototxt import serialize
text = serialize(dict, pretty=True)
```

Alternatively, from command line from this repo:

```commandline
$ python3 prototxt_parser_main.py prototxt_file
```
