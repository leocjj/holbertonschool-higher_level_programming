#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)

    for item in names:
        if not (item[0] == '_' and item[1] == '_'):
            print(item)


if __name__ == "__main__":
    main()
