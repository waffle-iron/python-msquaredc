"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mmsquaredc` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``msquaredc.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``msquaredc.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click


@click.command()
@click.argument('names', nargs=-1)
def main(names):
    """Console script for msquaredc"""
    gui = False
    if gui:
        from msquaredc.ui.gui.main import main
    else:
        from msquaredc.ui.tui.main import main
    main()
    click.echo(repr(names))


if __name__ == "__main__":  # pragma no cover
    main()
