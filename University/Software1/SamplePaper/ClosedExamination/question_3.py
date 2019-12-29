#!/usr/bin/env python3
def two_out_five(message):
    if not isinstance(message, str):
        raise TypeError("expected str")
    if len(message) % 5 != 0:
        raise ValueError("Message incorrect length")

    adders = [7, 4, 2, 1, 0]
    for i in range(0, len(message), 5):
        one_count = 0
        total = 0
        for j in range(0, 5):
            if message[i+j] == 1:
                one_count += 1
                total += adders
