#!/usr/bin/env python
import os
import tomlkit as TOML
import json as JSON
from ruamel.yaml import YAML


def getFileExt(filepath):
    filename, file_ext = os.path.splitext(filepath)

    # Standarize extensions
    if file_ext == 'yml':
        file_ext = 'yaml'

    return file_ext[1:]


def unserialize(serialized_str, format_hint):
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
        return JSON.loads(serialized_str)

    elif format_hint == 'yaml':
        return YAML().load(serialized_str)


def parse_file(filepath):
    """Read the config file into python data structures. The file at filepath
    must be readable by this process."""
    with open(filepath, 'r') as f:
        filecontent = f.read()
    file_ext = getFileExt(filepath)
    return unserialize(filecontent, file_ext)
