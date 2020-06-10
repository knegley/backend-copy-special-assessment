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
# import sys
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
        pattern = re.compile(r"[__](\w+)[__]")
        special_files = [item for item in files if pattern.search(item)]

        return (special_files)
    else:
        print("Path and Directory does not exist")


# code that ybrahim walked through for me ####################

    # special_files = []
    # list_paths = os.listdir(dirname)
    # for file in list_paths:
    #     pattern = re.search(r"[__](\w+)[__]", file)
    #     if pattern:
    #         special_files.append(os.path.abspath(
    #             (os.path.join(dirname, file))))

    # return special_files

#################################################################
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

    # Ybrahmim helped me properly use the shutil copy
    if not os.path.isdir(dest_dir):

        os.makedirs(dest_dir)
        # shutil.copy(os.path.abspath(path_list), os.path.abspath(directory))

    for item in path_list:
        path = os.path.join(dest_dir, os.path.basename(item))
        shutil.copy(item, path)

    # your code here
    # my junk code is below here that i tried before reaching out to ybrahim

    # if os.path.isdir(dest_dir):
    #     for item in path_list:

    #         if os.path.isfile(item):

    #             for _, _, file_name in os.walk(dest_dir):

    #                 if item in os.path.abspath(file_name):
    #                     print("file already exists in the dest_dir")
    #                     return
    #                 else:
    #                     shutil.copy(item, dest_dir)

    #  else:
    #    print(
    #   f"The path: {item} can't be copied because file doesn't exits")
    #             return
    # print(f"the directory {dest_dir} does not exist")
    # dir_response = input(
    # "would you like to create a directory w
    #   ith the path_list? respond Y or N\n")
    # if dir_response == "N":
    #     return
    # if dir_response == "Y":
    # os.mkdir(dest_dir)
    # destination = os.path.abspath(dest_dir)
    # print(destination)
    # print(os.path.exists(destination))
    # for item in path_list:
    # shutil.copytree(os.path.abspath("xyz_hello_.txt"), destination)
    # print(os.path.abspath(item))
    # print(os.path.realpath(item))
    # print(os.path.basename(item))
    # final_destination = os.path.join(os.path.basename(item))
    #     shutil.copy2(os.path.basename(item),
    #                  os.path.relpath(os.mkdir(dest_dir)))
    # curr_dir = os.getcwd()
    # destination = os.mkdir(dest_dir)
    # source_path = os.path.join(curr_dir, item)
    # shutil.copy2(os.path.abspath(item), destination)

# copy_to(["xyz_hello_.txt"], "something_cool")


def zip_to(path_list, dest_zip):

    for item in path_list:

        subprocess.run(["zip", "-j", dest_zip, item])
    return


def main():
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument("from_dir", help="return directory")
    args = parser.parse_args()
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
    main()
