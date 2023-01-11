#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or a_dictionary is None:
        return None
    new_key = list(a_dictionary.keys())[0]
    bigger = a_dictionary[new_key]
    for key, val in a_dictionary.items():
        if val > bigger:
            bigger = val
            new_key = key
    return new_key
