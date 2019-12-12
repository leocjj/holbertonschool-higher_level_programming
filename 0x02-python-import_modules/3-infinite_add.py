#!/usr/bin/python3
from sys import argv


def main():
    n = len(argv) - 1
    sum = 0

    if n == 0:
        print('0')
    elif n == 1:
        print('{}'.format(argv[1]))
    else:
        for i in range(1, n + 1):
            sum += int(argv[i])
        print('{}'.format(sum))


if __name__ == "__main__":
    main()
