#!/usr/bin/env python
import tomlkit as TOML
import json as JSON
from ruamel.yaml import YAML


def parse_content(str_to_parse, format_hint):
    """Parse a string in YAML, TOML or JSON format into python
    datastructures."""
    if format_hint == 'toml':
        return TOML.loads(str_to_parse)
    elif format_hint == 'json':
        return JSON.loads(str_to_parse)

    elif format_hint == 'yaml':
        return YAML().load(str_to_parse)



