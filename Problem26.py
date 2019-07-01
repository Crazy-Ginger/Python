#!/usr/bin/env python3
from decimal import *
getcontext().prec = 20

for i in range(1, 1000):
    temp = str((Decimal(1)/Decimal(i)))
    print (temp, "\t", len(temp))

