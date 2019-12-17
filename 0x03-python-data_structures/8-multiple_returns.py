#!/usr/bin/python3


def multiple_returns(sentence):

    tup = ()
    size = len(sentence)
    if size > 0:
        first = sentence[0]
    else:
        first = ''
    tup += (size,)
    tup += (first,)

    return tup
