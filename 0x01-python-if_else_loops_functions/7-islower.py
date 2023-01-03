#!/usr/bin/python3
def islower(c):
    n = ord(c)
    for i in range(97, 123):
        if (n == i):
            return True
    return False
