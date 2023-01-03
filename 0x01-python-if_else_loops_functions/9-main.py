#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

r = str(print_last_digit(98))+ ""
r += str(print_last_digit(0))
r += str(print_last_digit(-1024))
print(r)
