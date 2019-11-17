#!/usr/bin/env python3

#1
def is_power(a,b):
    if a == b or (a==1 and b!=0):
        return True
    elif b==0 or b==1 or a/b < b:
        return False
    else:
        return is_power(a/b, b)

#2
def sum_digits(number):
    number = str(number).strip('-')
    if len(number) > 0:
        return int(number[0]) + sum_digits(number[1:])
    else:
        return 0

#3
def rec_sum(numbers):
    if len(numbers)>0:
        return int(numbers[0]) + rec_sum(numbers[1:])
    else:
        return 0

#5
def flatten(mlist):
    if len(mlist) > 1:
        if type(mlist[0]) == list and len(mlist[0]) > 0:
            nlist = flatten(mlist[0])
            nlist += flatten(mlist[1:])

        else:
            nlist =  [mlist[0]]
            nlist = nlist + flatten(mlist[1:])

    else:
        if type(mlist[0]) == list:
            nlist = flatten(mlist[0])
        else:
            nlist = mlist
    print (nlist)
    return nlist


### Debug code
print (flatten([[1], [], [], [2,[],[3]]]))
