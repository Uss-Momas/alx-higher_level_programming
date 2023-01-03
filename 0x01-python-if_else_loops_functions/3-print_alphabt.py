#!/usr/bin/python3
n = 97
while n < 123:
    if (chr(n) != 'e') and (chr(n) != 'q'):
        print("{}".format(chr(n)), end='')
    n += 1
