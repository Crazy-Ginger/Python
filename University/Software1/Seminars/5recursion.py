#!/usr/bin/env python3

# probably non-functional and won't work
def sum_all(numbers):
    if len(numbers) > 1:
        if type(numbers[0])==list:
            return total + sum_all(numbers[0])
        else:
            return total + sum_all(numbers[1:])
    else:
        return number[0]

def to_binary(number):
    if number < 2:
        return number
    else:
        return  str(to_binary(number//2)) + str(number%2)


def to_base10(binary):
    if len(binary) == 1:
        return int(binary)
    else:
         return int(binary[0])*(2**(len(binary)-1)) + to_base10(binary[1:])

x = "83"
y = to_binary(x)
print (to_binary(x))
print (to_base10(y))
