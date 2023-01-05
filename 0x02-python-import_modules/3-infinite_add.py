#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    sum = 0
    args = len(argv) - 1
    if (args == 0):
        print(sum)
    else:
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print(f"{sum:d}")
