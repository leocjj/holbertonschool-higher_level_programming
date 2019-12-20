#!/usr/bin/python3

#that converts a Roman numeral to an integer.

#number will be between 1 to 3999.
#return an integer
#If the roman_string is not a string or None, return 0

def roman_to_int(roman_string):

    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}

    if (not isinstance(roman_string, str)) or (not roman_string):
        return 0

    num = [1, 5, 10, 50, 100, 500, 1000]
    roman = ["I", "V", "X", "L", "C", "D", "M"]
    result = 0
    prev = 1001
    for i in range(len(roman_string)):
        idx = roman.index(roman_string[i])
        if prev >= num[idx]:
            result = result + num[idx]
            prev = num[idx]
        else:
            result = num[idx] - 2 * prev + result
            prev = num[idx]
    return result
