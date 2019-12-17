#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    len_list = len(my_list)
    copy_list = my_list[:]
    if idx < 0:
        return copy_list
    elif idx >= len_list:
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list
    return
