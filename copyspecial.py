#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Kyle Negley and Ybrahim(COACH)"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    if os.path.exists(dirname) and os.path.isdir(dirname):
        with os.scandir(dirname) as directory:
            files = [os.path.abspath(os.path.join(dirname, item))
                     for item in directory if item.is_file()]
        pattern = re.compile(r"__(\w+)__")
        special_files = [item for item in files if pattern.search(item)]

        return (special_files)
    else:
        print("Path and Directory does not exist")


def copy_to(path_list, dest_dir):
    """ copies files to des_dir"""
    # Ybrahmim helped me properly use the shutil copy
    if not os.path.isdir(dest_dir):

        os.makedirs(dest_dir)
        # shutil.copy(os.path.abspath(path_list), os.path.abspath(directory))

    for item in path_list:
        path = os.path.join(dest_dir, os.path.basename(item))
        shutil.copy(item, path)


def zip_to(path_list, dest_zip):
    """creates zip dir"""
    for item in path_list:

        subprocess.run(["zip", "-j", dest_zip, item])
    return


def create_parser():
    """creates namespace with args"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument("from_dir", help="return directory")
    return parser


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = create_parser()

    args = parser.parse_args(args)
    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # listing out args from namespace from the parser
    from_dir = args.from_dir
    copy_to_dir = args.todir
    zip_dir = args.tozip

    special_paths = get_special_paths(from_dir)

    if copy_to_dir:
        copy_to(special_paths, copy_to_dir)
    elif zip_dir:
        zip_to(special_paths, zip_dir)
    else:
        print("\n".join((special_paths)))

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
