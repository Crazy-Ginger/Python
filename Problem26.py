#!/usr/bin/env python3
from decimal import *
getcontext().prec = 100
longer = 0
for i in range(1, 1000):
    temp = str((Decimal(1)/Decimal(i)))
    print (temp, "\t", len(temp))
    if (len(temp)>longer):
        longer = len(temp)

print("longest: ", longer)

