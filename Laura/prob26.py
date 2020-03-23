from decimal import *

getcontext().prec = 200
to_examine = [x for x in range(1000) if not (x % 5 == 0 or x % 2 == 0)]
decimals = [Decimal(1) / Decimal(x) for x in to_examine]
pairs = zip(to_examine, decimals)

repeaters = list()

for pair in pairs:
    reciprocal = str(pair[1])
    max_len = len(reciprocal)
    for test_length in range(2, max_len):
        repeater = reciprocal[:test_length]
        if (repeater * (max_len  // test_length) + 1)[:max_len] == reciprocal:
            repeaters.append(pair[0])
            break
