#!/usr/bin/python3


def delete_at(my_list=[], idx=0):

    size = len(my_list)

    if not my_list:
        return []
    if size == 0:
        return my_list
    if idx < 0:
        return my_list
    if idx >= size:
        return my_list

    del my_list[idx]

    return my_list
