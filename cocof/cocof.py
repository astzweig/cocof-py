#!/usr/bin/env python
import click


@click.command()
@click.argument('filepath', type=click.Path(
        exists=True,
        dir_okay=False,
        writable=True,
        resolve_path=True
    ))
def cli(filepath):
    """Cocof runs it's modifications on the configuration file given with
    the 'filepath' argument."""
    pass


if __name__ == '__main__':
    cli()
