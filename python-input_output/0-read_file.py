#!/usr/bin/python3
""" Write a func that reads a text file and prints it to stdout"""


def read_file(filename=""):
""" Read a file and prints it to stdout"""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")

