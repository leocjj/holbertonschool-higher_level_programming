#!/usr/bin/python3


def best_score(a_dictionary):

    if not a_dictionary:
        return None
    
    best = a_dictionary[sorted(a_dictionary.keys())[0]]
    for key in sorted(a_dictionary.keys()):
        if a_dictionary[key] > best:
            best = a_dictionary[key]
    return best
