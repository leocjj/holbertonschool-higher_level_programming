#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    result_list = []
    result = 0

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            result = 0
            print("division by 0")
            continue
        except TypeError:
            result = 0
            print("wrong type")
            continue
        except IndexError:
            result = 0
            print("out of range")
            continue
        except:
            result = 0
            continue
        finally:
            result_list += [result]

    return result_list
