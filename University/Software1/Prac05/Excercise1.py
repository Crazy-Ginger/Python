total = 0
for i in range(8*8):
    total += 2**i
    print (round(2**i *(3*pow(10,-5)),4), "kg")

print("Final mass:",round(total * (3*pow(10,-5)),5), "kg")
