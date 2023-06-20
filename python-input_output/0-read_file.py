#!/usr/bin/python3
""" Write a func that reads a text file and prints it to stdout"""


def read_file(filename=""):
    with open("my_file_0.txt", mode="r", encoding="utf-8") as filename:
        print(filename.read())
