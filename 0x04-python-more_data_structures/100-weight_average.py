#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    deno, avg = 0, 0
    for tup in my_list:
        avg += tup[0] * tup[1]
        deno += tup[1]
    return float(avg / deno)
