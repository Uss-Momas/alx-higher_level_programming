#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ro_str = roman_string
    value = 0
    for i in range(0, len(ro_str)):
        if (i + 1) != len(ro_str):
            prev, next_v = letters[ro_str[i]], letters[ro_str[i + 1]]
            if prev >= next_v:
                value += prev
            else:
                value -= prev
        else:
            value += letters[ro_str[i]]
    return value
