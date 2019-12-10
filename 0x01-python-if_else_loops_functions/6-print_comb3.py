#!/usr/bin/python3

i = 0

for num in range(1, 101, 10):
    for num2 in range(num, num + 9):
        if num2 > i:
            print('{:02}'.format(num2), end='')
            if num2 < 88:
                print(', ', end='')
    i += 11
print()
