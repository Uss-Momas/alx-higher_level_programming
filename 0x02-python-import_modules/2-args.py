#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    number_args = len(argv) - 1
    if number_args == 0:
        print("0 arguments.")
    elif number_args == 1:
        print(f"1 argument:\n1: {argv[1]}")
    else:
        print("{} arguments:".format(number_args))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
