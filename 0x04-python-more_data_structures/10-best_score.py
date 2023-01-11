#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or a_dictionary is None:
        return None
    new_key = list(a_dictionary.keys())[0]
    value = a_dictionary[new_key]
    for key in a_dictionary:
        if a_dictionary[key] >= value:
            new_key = key
    return new_key
