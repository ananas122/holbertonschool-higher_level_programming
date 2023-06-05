#!/usr/bin/python3
a = 89
b = 10
# switch a and b
a, b = b, a
print(a, b)  # 10
print(b, a)  # 89
print("a={:d} - b={:d}".format(a, b))
