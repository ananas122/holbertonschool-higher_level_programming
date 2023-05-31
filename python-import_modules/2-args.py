#!/usr/bin/python3
import sys

if __name__ == '__main__':
    # print(sys.argv)
    arguments = sys.argv[1:]
    # print(arguments)
    num_arguments = len(sys.argv) - 1
#    print(num_arguments)
    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument")
        print(f"1: {arguments[0]}")

    else:
        print(f"{num_arguments} arguments:")
        for i in range(num_arguments):
            print(f"{i}: {arguments[i]}")
