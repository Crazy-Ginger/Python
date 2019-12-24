#!/usr/bin/env python3

def detect_correct(word):
    """Function returns a tuple with string of bits and number of errors passed in input"""
    if not isinstance(word, str):
        raise TypeError
    elif len(word) % 3 != 0:
        raise ValueError
    bits = ""
    errors = 0
    for i in range(0, len(word), 3):
        bit_sum = 0
        for j in range(3):
            if int(word[i+j]) > 1:
                raise ValueError
            bit_sum += int(word[i+j])
        if bit_sum == 3:
            bits += "1"
        elif bit_sum == 0:
            bits += "0"
        else:
            errors += 1
            if bit_sum == 2:
                bits +="1"
            else:
                bits += "0"
    return (bits, errors)
