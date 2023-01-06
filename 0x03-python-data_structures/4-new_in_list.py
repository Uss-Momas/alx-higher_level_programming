#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = list(my_list)
    if idx < 0:
        return cp_list
    if idx >= len(my_list):
        return cp_list
    for i in cp_list:
        if i == idx:
            cp_list[i] = element
    return cp_list
