#!/usr/bin/python
# coding: utf-8 -*-

import os
import sys
import json
from typing import List
import shutil


def get_license_files(folder: str, lic_extension: str = '.json') -> List[str]:
    """Get list of files in a folder"""
    onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    return [f for f in onlyfiles if f.endswith(lic_extension)]


def filename_builder(customer: str, serial: str, end_str: str = '-lic.json') -> str:
    """Build filename to use instead of default one."""
    return f'{customer.upper()}-{serial}{end_str}'


def rename_license_file(folder_path: str, filename: str, backup: bool = True):
    """
    Entrypoint to rename license file.

    For a license file, it reads content for customer and serial
    then rename file with these values.
    If backup is set, then also copy initial version to backup folder

    Args:
        folder_path (str): Folder where license file is.
        filename (str): Name of license file
        backup (bool, optional): Enable a backup of original file. Defaults to True.

    Returns:
        str: New filename
    """
    serial : str
    customer: str
    # Opening JSON file
    with open(f'{folder_path}/{filename}') as lic_file:
        lic = json.loads(lic_file.read())
    if 'BindingInfo' in lic and 'SerialNumber' in lic['BindingInfo']:
        serial = lic['BindingInfo']['SerialNumber']
    if 'CustomerName' in lic:
        customer = lic['CustomerName']

    lic_new_filename = filename_builder(customer=customer, serial=serial)

    if backup:
        path = os.path.join(folder_path, 'backup')
        os.makedirs(path, exist_ok=True)
        shutil.copy(f'{folder_path}/{filename}', path)

    shutil.move(f'{folder_path}/{filename}',f'{folder_path}/{lic_new_filename}')
    return lic_new_filename

