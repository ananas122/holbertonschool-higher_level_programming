#!/usr/bin/python3
""" Write a function that creates an Obj from a JSON file"""
import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)