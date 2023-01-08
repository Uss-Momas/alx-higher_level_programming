#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
   # if (len(tuple_a) and len(tuple_b)) == 2:
   #     return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    tuple_c = tuple(zip(tuple_a, tuple_b))
    result = sum(tuple_c[0]), sum(tuple_c[1])
    return tuple_c
