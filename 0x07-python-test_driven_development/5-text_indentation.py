#!/usr/bin/python3
"""This module prints a text with 2 new lines after each of these chars . ?  :

    text must be a string
        otherwise raise TypeError('text must be a string')

    There should be no space at the beginning or at the end of each line

    You are not allowed to import any module

    Returns nothing

    This module supplies one function, text_indentation().  For example,

    >>> text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing
    elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas?)
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <BLACKLINE>
    Quonam modo?
    <BLACKLINE>
    Utrum igitur tibi litteram videor an totas paginas?
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: . ?  :

    Args:
        text: the first name.

    Returns:
        None: returns nothing.

    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    newline_ = True

    for char_ in text:
        if newline_ and char_ is ' ':
            continue

        if char_ in '.?:':
            print(char_)
            print()
            newline_ = True
        else:
            print(char_, end='')
            newline_ = False

    # while i < len_:
    #     if temp[i] in '.?:':
    #         if i + 1 < len_:
    #             temp[i + 1] = '\n'
    #         print(temp[i], end='')
    #         print()
    #         i += 1
    #         continue
    #     else:
    #         if i - 1 >= 0:
    #             if (temp[i - 1] == '\n' or (i - 1) == 0) and temp[i] == ' ':
    #                 del temp[i]
    #                 len_ -= 1
    #         print(temp[i], end='')
    #         i += 1
