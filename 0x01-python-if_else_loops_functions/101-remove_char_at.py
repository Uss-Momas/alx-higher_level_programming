#!/usr/bin/python3
def remove_char_at(str, n):
    cpy_str = ""
    if n > len(str) or n < 0:
        return str
    for i in range(0, len(str)):
        if i != n:
            cpy_str += str[i]
    return cpy_str
