#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or a_dictionary is None:
        return None
    max_value = max(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary[key] == max_value:
            return key
    return None
