#!/usr/bin/python3

"""
Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    new_text = ""
    for char in text:
        if char in [".", "?", ":"]:
            new_text += char + "\n\n"
        elif char != " ":
            new_text += char

    print(new_text, end='')
