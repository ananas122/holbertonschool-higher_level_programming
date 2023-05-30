#!/usr/bin/python3
def uppercase(str):
    uppercase = 0
    for i in str:
        if(ord(i) >= 97 and ord(i) <= 122):
            uppercase = 32
        else:
            uppercase = 0
        print("{}".format(chr(ord(i) - uppercase)), end='')
    print()

#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")
