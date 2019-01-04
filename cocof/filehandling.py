#!/usr/bin/env python
# coding: utf-8
import os
import tomlkit as TOML
import json as JSON
from collections import OrderedDict
from click import open_file
from ruamel.yaml import (
        round_trip_load as yaml_deserialize,
        round_trip_dump as yaml_serialize
)


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
    return format_hint


def deserialize(serialized_str, format_hint):
    """Parse a string in YAML, TOML or JSON format into python
    datastructures.

    Args:
        serialized_str (str):  The YAML, JSON or TOML string.
        format_hint (str): The format of 'serialized_str'. Either one of:
                           yaml, toml or json.
    """
    if format_hint == 'toml':
        return TOML.loads(serialized_str)

    elif format_hint == 'json':
        # Use ordered dict, to keep order of keys as readed.
        return JSON.loads(serialized_str, object_pairs_hook=OrderedDict)

    elif format_hint == 'yaml':
        return yaml_deserialize(serialized_str)


def serialize(datastructure, format_hint):
    """Serialize the datastructure to either YAML, TOML or JSON string.

    Args:
        datastructure (any): The datastructure to serialize into a string
                             using 'format_hint' format.
        format_hint (str): see 'unserialize'.
    """
    if format_hint == 'toml':
        return TOML.dumps(datastructure)

    elif format_hint == 'json':
        output = JSON.dumps(datastructure, indent=2)
        # Remove whitespace before line breaks (needed for Python2.7)
        return output.replace(' \n', '\n')

    elif format_hint == 'yaml':
        return yaml_serialize(datastructure)[:-1]


def parse_file(filepath, format_hint=None):
    """Read the config file into python data structures. The file at filepath
    must be readable by this process."""
    format_hint = guessFileFormat(filepath, format_hint)
    with open_file(filepath, 'r') as f:
        filecontent = f.read()
    return deserialize(filecontent, format_hint)


def write_to_file(filepath, datastructure, format_hint=None):
    """Write the datastructure into the conifg file at 'filepath'."""
    format_hint = guessFileFormat(filepath, format_hint)
    serialized = serialize(datastructure, format_hint)
    with open_file(filepath, 'w') as f:
        f.write(serialized)
