#!/usr/bin/env python
# coding: utf-8
import click
from jsonpatch import JsonPatch
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError
from .filehandling import parse_file, write_to_file


@click.command()
@click.option('-f', '--format', 'file_format',
              type=click.Choice(['toml', 'yaml', 'json']),
              required=False,
              default=None,
              help='The format of the file. Obligatory if filepath is \'-\''
                   ' (stdin).')
@click.argument('filepath', type=click.Path(
        exists=True,
        allow_dash=True,
        dir_okay=False,
        writable=True,
        resolve_path=True
    ))
@click.argument('jsonpatch')
def cli(filepath, jsonpatch, file_format):
    """Cocof runs the provided 'jsonpatch' modifications on the configuration
    file given with the 'filepath' argument. Use the '--format' option to
    tell the file format. If not given cocof will try to guess the file format
    based on the file extension. Use '-' as filepath for stdin,
    in which case the output goes to stdout and you must provide the format of
    the data via the '--format' option."""
    try:
        data = parse_file(filepath, file_format)
        patch = JsonPatch.from_string(jsonpatch)
        result = patch.apply(data)
        write_to_file(filepath, result, file_format)
    except (JSONDecodeError, TypeError):
        click.secho('ERROR: Invalid jsonpatch provided. A possible solution'
                    ' would be to verify the jsonpatch using an online'
                    'verifier.', fg='red', err=True)
        return 102
    except BaseException as e:
        click.secho('Error: Something went wrong. Developer info: ' + str(e),
                    fg='red', err=True)
        return 101
    return 0


if __name__ == '__main__':
    cli()
