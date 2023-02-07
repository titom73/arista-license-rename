#!/usr/bin/env python
# coding: utf-8 -*-
# pylint: disable=no-value-for-parameter
# pylint: disable=cyclic-import
# pylint: disable=too-many-arguments


import click
from rich.console import Console
import eos_license
from eos_license.cli import commands as generic_commands


@click.group()
def ar_lic_cleaner() -> None:
    """Arista Network Download CLI"""
    pass


@click.command()
def info():
    """Display version of ardl"""
    console = Console()
    console.print(f'Arista License Cleaner is running version {eos_license.__version__}')


def cli() -> None:
    """Load ANTA CLI"""
    # Load group commands
    ar_lic_cleaner.add_command(info)
    ar_lic_cleaner.add_command(generic_commands.rename)
    # Load CLI
    ar_lic_cleaner(
        obj={},
        auto_envvar_prefix='arista'
    )


if __name__ == '__main__':
    cli()