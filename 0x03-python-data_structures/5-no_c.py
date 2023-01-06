#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for el in my_string:
        if ord(el) != ord('c') and ord(el) != ord('C'):
            string += el
    return string
