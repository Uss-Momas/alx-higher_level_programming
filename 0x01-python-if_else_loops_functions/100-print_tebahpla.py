#!/usr/bin/python3
lower = 122
upper = 89
while lower >= 97:
    if (lower % 2 == 0) and (upper % 2 != 0):
        print("{}".format(chr(lower)), end="")
    if (upper % 2 != 0):
        print("{}".format(chr(upper)), end="")
    lower = lower - 1
    upper -= 1
