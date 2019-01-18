#!/usr/bin/env python
# coding: utf-8
import os
import tomlkit as TOML
import json as JSON
import biplist as PLIST
from collections import OrderedDict
from click import open_file
from ruamel.yaml import (
        round_trip_load as yaml_deserialize,
        round_trip_dump as yaml_serialize
)
try:
    unicode
except:
    unicode = str


def getFileExt(filepath):
    filename, file_ext = os.path.splitext(filepath)

    # Standarize extensions
    if file_ext == '.yml':
        file_ext = '.yaml'

    return file_ext[1:]


def guessFileFormat(filepath, format_hint):
    if format_hint is None:
        format_hint = getFileExt(filepath)
        if format_hint == '':
            raise ValueError('Cannot figure out file format.')

    if format_hint == 'plist':
        with open_file(filepath, 'rb') as f:
            f.seek(0)
            if f.read(7) == b'bplist0':
                format_hint = 'plist_binary'

    return format_hint


def deserialize(serialized, format_hint):
    """Parse a string in YAML, TOML, JSON or PLIST format into python
    datastructures.

    Args:
        serialized (str, bytes):  The YAML, TOML, JSON or PLIST content.
        format_hint (str): The format of 'serialized_str'. Either one
                           of: yaml, toml, json or plist.
    """
    try:
        serialized = serialized.decode('utf-8')
    except UnicodeDecodeError:
        pass

    if format_hint == 'toml':
        return TOML.loads(serialized)

    elif format_hint == 'yaml':
        return yaml_deserialize(serialized)

    elif format_hint == 'json':
        # Use ordered dict, to keep order of keys as readed.
        return JSON.loads(serialized, object_pairs_hook=OrderedDict)

    elif format_hint == 'plist' or format_hint == 'plist_binary':
        if isinstance(serialized, unicode):
            serialized = serialized.encode('utf-8')
        return PLIST.readPlistFromString(serialized)


def serialize(datastructure, format_hint):
    """Serialize the datastructure to either YAML, TOML, JSON  or PLIST
    string (or bytes).

    Args:
        datastructure (any): The datastructure to serialize into a string
                             using 'format_hint' format.
        format_hint (str): see 'unserialize'.
    """
    if format_hint == 'toml':
        return TOML.dumps(datastructure)

    elif format_hint == 'yaml':
        return yaml_serialize(datastructure)[:-1]

    elif format_hint == 'json':
        output = JSON.dumps(datastructure, indent=2)
        # Remove whitespace before line breaks (needed for Python2.7)
        return output.replace(' \n', '\n')

    elif format_hint == 'plist' or format_hint == 'plist_binary':
        write_as_binary = format_hint == 'plist_binary'
        output = PLIST.writePlistToString(datastructure, write_as_binary)
        # Remove whitespace before line breaks (needed for Python2.7)
        return output.rstrip()


def parse_file(filepath, format_hint=None):
    """Read the config file into python data structures. The file at filepath
    must be readable by this process. If the file is not encoded as
    utf-8 it will be read as a binary file."""
    format_hint = guessFileFormat(filepath, format_hint)
    with open_file(filepath, 'rb') as f:
        filecontent = f.read()
    return deserialize(filecontent, format_hint)


def write_to_file(filepath, datastructure, format_hint=None):
    """Write the datastructure into the conifg file at 'filepath'."""
    format_hint = guessFileFormat(filepath, format_hint)
    serialized = serialize(datastructure, format_hint)
    if isinstance(serialized, str) and format_hint.endswith('_binary'):
        serialized = serialized.encode('utf-8')
    with open_file(filepath, 'wb') as f:
        f.write(serialized)
