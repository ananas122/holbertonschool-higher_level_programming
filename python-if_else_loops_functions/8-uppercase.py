#!/usr/bin/python3
def uppercase(str):
    uppercase = 0
    for alphabet in str:
        if (ord(alphabet) >= 97 and ord(alphabet) <= 122):
            uppercase = 32
        else:
            uppercase = 0
        print("{}".format(chr(ord(alphabet) - uppercase)), end='')
    print()
