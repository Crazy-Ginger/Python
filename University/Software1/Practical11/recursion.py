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
    print ("mlist:",mlist, "length:", len(mlist))
    if len(mlist) == 0:
        pass

    elif type(mlist[0]) != list and len(mlist) > 1:
        print ("#1")
        nlist = [mlist[0]]
        print ("nlist:",nlist)
        nlist.append(flatten(mlist[1:]))
        return nlist

    elif type(mlist[0]) == list:
        print ("#2")
        nlist = [flatten(mlist[0])]
        return nlist

    elif len(mlist) == 1:
        print ("#3")
        return mlist[0]


### Debug code
x = flatten([1,2,3,4])
print (x,"\n\n\n")

print (flatten([1,2,[3,4,],5]))
