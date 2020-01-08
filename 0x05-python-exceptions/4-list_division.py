#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):


    result_list = []

    for i in range(list_length):
        try:
            result_list += [my_list_1[i] / my_list_2[i]]

        except ZeroDivisionError:
            result_list += [0]
            print("division by 0")
            continue
        except TypeError:
            result_list += [0]
            print("wrong type")
            continue
        except IndexError:
            result_list += [0]
            print("out of range")
            continue
        except:
            result_list += [0]
            continue

    return result_list
