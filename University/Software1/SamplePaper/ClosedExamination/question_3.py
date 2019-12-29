#!/usr/bin/env python3
def two_out_five(message):
    if not isinstance(message, str):
        raise TypeError("expected str")
    if len(message) % 5 != 0:
        raise ValueError("Message incorrect length")

    adders = [7, 4, 2, 1, 0]
    final_total = ""
    for i in range(0, len(message), 5):
        one_count = 0
        total = 0
        for j in range(0, 5):
            if message[i+j] == "1":
                one_count += 1
                total += adders[i+j]
            elif message[i+j] != "0":
                print ("message[",i,"+",j,"]: ", message[i+j])
                raise ValueError("Exptected only 1's and 0's in input")
            elif one_count > 2:
                print ("one_count",one_count)
                raise ValueError ("Too many 1's in input")
        if total == 11:
            final_total += "0"
        else:
            final_total += str(total)
    return final_total
