#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "???"

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
            files = [os.path.abspath(item)
                     for item in directory if item.is_file()]
            # for item in directory:
            #     # print(item)
            #     # print(item.is_file())
            #     if item.is_file():
            #         print(os.path.abspath(item))
            # print("\n".join(files))

        return "\n".join(files)
    else:
        print("Path and Directory does not exist")


# print(os.getcwd())
# print(get_special_paths(os.getcwd()))
# (get_special_paths("helloasdfage"))
# print(os.listdir(os.getcwd()))
# with os.scandir(os.getcwd()) as test_direcotry:
#     for item in test_direcotry:
#         print(item)


# for dir_path, dirname, filename in os.walk(os.getcwd()):
#     if dirname:
#         print(f"dirname: {dirname}")
#     if "copyspecial.py" in filename:
#         print("copy file is here")

# print(filename)


def copy_to(path_list, dest_dir):
    # your code here

    # if os.path.isdir(dest_dir):
    #     for item in path_list:

    #         if os.path.isfile(item):

    #             for _, _, file_name in os.walk(dest_dir):

    #                 if item in os.path.abspath(file_name):
    #                     print("file already exists in the dest_dir")
    #                     return
    #                 else:
    #                     shutil.copy(item, dest_dir)

    #             else:
    #                 print(
    #                     f"The path: {item} can't be copied because file doesn't exits")
    #             return
    # print(f"the directory {dest_dir} does not exist")
    # dir_response = input(
    #     "would you like to create a directory with the path_list? respond Y or N\n")
    # if dir_response == "N":
    #     return
    # if dir_response == "Y":
    # os.mkdir(dest_dir)
    # destination = os.path.abspath(dest_dir)
    # print(destination)
    # print(os.path.exists(destination))
    for item in path_list:
        # shutil.copytree(os.path.abspath("xyz_hello_.txt"), destination)
        # print(os.path.abspath(item))
        # print(os.path.realpath(item))
        # print(os.path.basename(item))
        # final_destination = os.path.join(os.path.basename(item))
        #     shutil.copy2(os.path.basename(item),
        #                  os.path.relpath(os.mkdir(dest_dir)))
        curr_dir = os.getcwd()
        destination = os.mkdir(dest_dir)
        source_path = os.path.join(curr_dir, item)
        shutil.copy2(os.path.abspath(item), destination)
    return


copy_to(["xyz_hello_.txt"], "something_cool")


def zip_to(path_list, dest_zip):
    # your code here
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
