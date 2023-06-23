#!/usr/bin/python3
"""
    To add all command-line args starting from the second one to the list,
    saves the updated list back to the file using the "save_to_json_file"
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


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
