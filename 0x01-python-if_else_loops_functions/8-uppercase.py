#!/usr/bin/python3


def uppercase(str):
    down = 0
    for char in str:
        if (char >= 'a') and (char <= 'z'):
            down = 32
        else:
            down = 0
        print('{:c}'.format(ord(char) - down), end="")
    print()
