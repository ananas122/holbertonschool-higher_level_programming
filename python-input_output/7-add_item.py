#!/usr/bin/python3
"""
    To add all command-line args starting from the second one to the list,
    saves the updated list back to the file using the "save_to_json_file"
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Load the existing list from the JSON file, or create an empty list
try:
    # Try to open the "add_item.json" file in read mode
    with open("add_item.json", "r") as f:
        # Load the list from the file using the json.load function
        my_list = json.load(f)
# If the file doesn't exist, create an empty list
except FileNotFoundError:
    my_list = []

# Add each argument to the list
for arg in args:
    my_list.append(arg)

# Open the file in write mode
with open("add_item.json", "w") as file:
    # Write the list to the file as JSON
    json.dump(my_list, file)
