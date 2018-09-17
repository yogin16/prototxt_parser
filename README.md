## prototxt-parser

prototxt-parser allows to parse `*.prototxt` files to python dict objects

### Usage:

From command line:
```commandline
$ python3 prototxt_parser.py prototxt_file
```

From python:
```python
input_string = ... # the prototxt string to be parsed
from prototxt_parser.prototxt import parse
parsed_dict = parse(input_string)
```

