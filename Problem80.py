#!/usr/bin/env python3
from decimal import *
total = 0
#sets the number of decimal places for floats to 100
getcontext().prec = 101

for i in range(1, 100):
    numb = str(Decimal(i).sqrt())
    temp = 0
    numb = numb[:-1]
    if len(numb) != 1:
        for char in numb:
            if char != '.':
                temp += int(char)
                total += int(char)
        print(i, "\tadding: ", temp)
        # print("total: ", total, "\n")
print("Total: ", total)
