#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1
        # com comprehension fica: [print (i) for i in my_list[::-1]]
