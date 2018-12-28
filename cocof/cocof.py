#!/usr/bin/env python
import click
from jsonpatch import JsonPatch
from json.decoder import JSONDecodeError
from .filehandling import parse_file, write_to_file


@click.command()
@click.argument('filepath', type=click.Path(
        exists=True,
        dir_okay=False,
        writable=True,
        resolve_path=True
    ))
@click.argument('jsonpatch')
def cli(filepath, jsonpatch):
    """Cocof runs the provided 'jsonpatch' modifications on the configuration
    file given with the 'filepath' argument."""
    data = parse_file(filepath)
    try:
        patch = JsonPatch.from_string(jsonpatch)
        result = patch.apply(data)
        write_to_file(filepath, result)
    except JSONDecodeError as e:
        click.secho('ERROR: Invalid jsonpatch provided. A possible solution'
                    ' would be to verify the jsonpatch using an online'
                    'verifier.', fg='red', err=True)
        return 101
    return 0


if __name__ == '__main__':
    cli()
