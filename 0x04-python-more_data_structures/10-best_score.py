#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    new_key = list(a_dictionary.keys())[0]
    bigger = a_dictionary[new_key]
    for key, val in a_dictionary.items():
        if val > bigger:
            bigger = val
            new_key = key
    return new_key
