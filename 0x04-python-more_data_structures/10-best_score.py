#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = max(a_dictionary.values())
    for value in a_dictionary.values():
        print(value, end=" ")
    return max_value
