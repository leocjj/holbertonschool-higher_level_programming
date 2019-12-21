#!/usr/bin/python3


def weight_average(my_list=[]):

    average = 0
    counter = 0

    if not my_list:
        return 0

    for num in my_list:
        average += num[0]*num[1]
        counter += num[1]
    if counter > 0:
        return (average/counter)
    else:
        return 0
