#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {"I": 1, "V": 5, "X": 10, "L": 50,
                "C": 100, "D": 500, "M": 1000}
    if type(roman_string) is str:
        return (0)
    number = 0
    skip = False
    for letter in range(len(roman_string)):
        if skip:
            skip = False
            continue
        if letter + 1 < len(roman_string):
            if numerals[roman_string[letter]] < \
                    numerals[roman_string[letter + 1]]:
                skip = True
                number += numerals[roman_string[letter + 1]]\
                    - numerals[roman_string[letter]]
                continue
        number += numerals[roman_string[letter]]
    return (number)
