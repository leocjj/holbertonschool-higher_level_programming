#!/usr/bin/python3


def no_c(my_string):

    copy_string = ''
    for item in range(len(my_string) - 1):
        if (my_string[item] != 'c') and (my_string[item] != 'C'):
            copy_string += my_string[item]
    return copy_string
