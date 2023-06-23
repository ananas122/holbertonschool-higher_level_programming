#!/usr/bin/python3
"""
    To add all command-line args starting from the second one to the list,
    saves the updated list back to the file using the "save_to_json_file"
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    # Try to load the list from the "add_item.json" file using the file 6
    json_list = load_from_json_file("add_item.json")

    # Add each argument passed in the command line to the list
    for item in sys.argv[1:]:
        json_list.append(item)

    # Save the updated list to the "add_item.json" file using file 5
    save_to_json_file(json_list, "add_item.json")

# If exceptions, save the args passed in the command line to the file instead
except Exception:
    save_to_json_file(sys.argv[1:], "add_item.json")
