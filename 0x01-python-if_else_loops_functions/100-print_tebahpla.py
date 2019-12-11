#!/usr/bin/python3


for char in range(122, 96, -2):
    print('{:c}{:c}'.format(char, char - 33), end='')
