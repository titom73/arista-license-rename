#!/usr/bin/env python
# coding: utf-8 -*-
# pylint: disable=no-value-for-parameter
# pylint: disable=too-many-arguments
# pylint: disable=line-too-long
# flake8: noqa E501

"""
Commands for ARDL CLI to get data.
"""

import click
from rich.console import Console
from eos_license import utils


@click.command()
@click.option('--input', '-i', help='Path where license files are located', type=click.Path())
@click.option('--backup/--no-backup', help='Save original lic under input/backup', default=True)
def rename(input: str, backup: bool) -> None:
    console = Console()
    console.print(f'Start reading folder [red]{input}[/red] for license file')
    lic_files = utils.get_license_files(folder=input)
    for lic in lic_files:
        renamed_file = utils.rename_license_file(folder_path=input, filename=lic, backup=backup)
        console.print(f'- License file: [red]{lic}[/red] renamed to [green]{renamed_file}[/green]')
