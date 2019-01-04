# Cocof
[![Build Status](https://travis-ci.org/astzweig/cocof-py.svg?branch=master)](https://travis-ci.org/astzweig/cocof-py)
[![PyPI version](https://badge.fury.io/py/cocof.svg)](https://badge.fury.io/py/cocof)

Cocof, short for consistent config file, is a python module that allows the
modification of different key-value config files on the comand line.

Most importantly: _It will keep line breaks and comments the same._ So the file
will look more or less like the original (depending on the operations on it of
course).

Currently supported formats are TOML, YAML and JSON.

### Install
```bash
$ pip install cocof
```

### Usage
```bash
$ cocof --help
Usage: cocof [OPTIONS] FILEPATH JSONPATCH

  Cocof runs the provided 'jsonpatch' modifications on the configuration
  file given with the 'filepath' argument. Use the '--format' option to tell
  the file format. If not given cocof will try to guess the file format
  based on the file extension. Use '-' as filepath for stdin, in which case
  the output goes to stdout and you must provide the format of the data via
  the '--format' option.

Options:
  -f, --format [toml|yaml|json]  The format of the file. Obligatory if
                                 filepath is '-' (stdin).
  --help                         Show this message and exit.
```

Cocof takes a file path and a [JSON patch][json_patch] string as arguments.
It then modifies the datastructure given by the file's content accordingly and
writies it back to the same file (in-place editing).
You can also tell `cocof` to read from `stdin`, in which case it will output
it's result to `stdout`.


### Examples
```TOML
# example.toml
title = "Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00 # Inline comment

[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
```

Using `{"op": "add", "path": "/subtitle", "value": "Sub"}` as modification
yields:

```bash
$ cocof ./example.toml '[{"op": "add", "path": "/subtitle", "value": "Sub"}]'`
$ cat ./example.toml
# example.toml
title = "Example"
subtitle = "Sub"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00 # Inline comment

[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
```

[json_patch]: https://tools.ietf.org/html/rfc6902
