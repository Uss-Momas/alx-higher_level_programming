#!/usr/bin/python3
from sys import argv, exit
import calculator_1 as calc


def main():
    args = len(argv) - 1
    if (args != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        if op == '+':
            print("{} {} {} = {}".format(a, op, b, calc.add(a, b)))
        elif op == '-':
            print("{} {} {} = {}".format(a, op, b, calc.sub(a, b)))
        elif op == '*':
            print("{} {} {} = {}".format(a, op, b, calc.mul(a, b)))
        elif op == '/':
            print("{} {} {} = {}".format(a, op, b, calc.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == '__main__':
    main()
