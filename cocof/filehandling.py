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


def parse_content(str_to_parse, format_hint):
    """Parse a string in YAML, TOML or JSON format into python
    datastructures."""
    if format_hint == 'toml':
        return TOML.loads(str_to_parse)
    elif format_hint == 'json':
        return JSON.loads(str_to_parse)

    elif format_hint == 'yaml':
        return YAML().load(str_to_parse)


def parse_file(filepath):
    """Read the config file into python data structures. The file at filepath
    must be readable by this process."""
    with open(filepath, 'r') as f:
        filecontent = f.read()
    file_ext = getFileExt(filepath)
    return parse_content(filecontent, file_ext)
