#!/usr/bin/python3
"""
imports the "save_to_json_file" and "load_from_json_file" functions from their respective files,
    attempts to load a list from a file named "add_item.json", and creates an empty list if it does not exist.
    The script then adds all command-line arguments starting from the second one to the list,
    and saves the updated list back to the file using the "save_to_json_file" function.
    """
import json
import sys

from my module import save_to_json_file, load_from_json_file

    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, "add_item.json")

