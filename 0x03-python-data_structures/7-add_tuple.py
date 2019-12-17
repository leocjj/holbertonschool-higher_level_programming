#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    I, J = len(tuple_a), len(tuple_b)
    ta, tb, tc = tuple_a, tuple_b, ()
    if I == 0:
        ta = (0, 0)
    if I == 1:
        ta += (0, )
    if J == 0:
        tb = (0, 0)
    if J == 1:
        tb += (0, )

    for i in range(2):
        tc += (ta[i] + tb[i],)

    return tc
