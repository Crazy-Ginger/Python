#!/usr/bin/env python3

def is_power(a,b):
    if a == b or (a==1 and b!=0):
        return True
    elif b==0 or b==1 or a/b < b:
        return False
    else:
        return is_power(a/b, b)

def sum_digits(number):
    number = str(number).strip('-')
    if len(number) > 0:
        return int(number[0]) + sum_digits(number[1:])
    else:
        return 0

def rec_sum(numbers):
    if len(numbers)>0:
        return int(numbers[0]) + rec_sum(numbers[1:])
    else:
        return 0

### gave up due to boredom
def flatten(mlist):
    if len(mlist) > 1:
        rlist = [mlist[0]]
        print (rlist)
        rlist = rlist.append(flatten(mlist[1:]))
        return rlist
    elif len(mlist) == 1:
        return mlist[0]
    
