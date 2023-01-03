#!/usr/bin/python3
def uppercase(str):
    base = ""
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:  # It means that is lower
            upper = ord(str[i]) - 32
            base += chr(upper)
        else:  # It means that the char at idx i is Uppercase
            base += str[i]
    print("{}".format(base))
