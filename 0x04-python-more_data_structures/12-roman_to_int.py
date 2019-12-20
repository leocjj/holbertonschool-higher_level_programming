#!/usr/bin/python3


def roman_to_int(roman_string):

    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}

    if (not isinstance(roman_string, str)) or (not roman_string):
        return 0

    num = [1, 5, 10, 50, 100, 500, 1000]
    roman = ["I", "V", "X", "L", "C", "D", "M"]
    result = 0
    prev = 1001

    for i in range(len(roman_string)):

        char = roman.index(roman_string[i])

        if prev >= num[char]:
            result += num[char]
            prev = num[char]
        else:
            result += num[char] - 2 * prev
            prev = num[char]

    return result
