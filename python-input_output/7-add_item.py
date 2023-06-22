#!/usr/bin/python3
"""
imports the "save_to_json_file" and "load_from_json_file" functions from their respective files,
    attempts to load a list from a file named "add_item.json", and creates an empty list if it does not exist.
    The script then adds all command-line arguments starting from the second one to the list,
    and saves the updated list back to the file using the "save_to_json_file" function.
    """
import json
import sys

# Retrieve all arguments passed to the script
args = sys.argv[1:]

# Create an empty list to store the arguments
my_list = []

# Add each argument to the list
for arg in args:
    my_list.append(arg)

# Open the file in write mode
with open("add_item.json", "w") as file:
    # Write the list to the file as JSON
    json.dump(my_list, file)
