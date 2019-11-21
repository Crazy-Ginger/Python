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
def __call_flatten(mlist):
    nlist = "Empty"
    if not mlist:
        return mlist
    elif len(mlist) > 1:
        if type(mlist[0]) == list:
            if len(mlist[0]) > 0:
                nlist = flatten(mlist[0]) + flatten(mlist[1:])
            elif len(mlist[0]) == 0:
                nlist = flatten(mlist[1:])
            else:
                pass

        else:
            nlist =  [mlist[0]] + flatten(mlist[1:])

    else:
        if type(mlist[0]) == list:
            if len(mlist[0]) > 0:
                nlist = flatten(mlist[0])
            elif len(mlist[0]) == 0:
                nlist = flatten(mlist[1:])
            else:
                pass
        else:
            nlist = mlist

    return nlist

def flatten(mlist):
    return __call_flatten(mlist.copy())

#6
def merge(sorted_listA, sorted_listB):
    sorted_list = []
    if len(sorted_listA) > 0 and len(sorted_listB) > 0:
        if sorted_listA <= sorted_listB:
            sorted_list.append(sorted_listA[0])
            sorted_list += merge(sorted_listA[1:], sorted_listB)

        else:
            sorted_list.append(sorted_listB[0])
            sorted_list += merge(sorted_listA,sorted_listB[1:])

    elif len(sorted_listA) == 0:
        sorted_list += sorted_listB

    elif len(sorted_listB) == 0:
        sorted_list += sorted_listA

    else:
        print ("Error")

    return sorted_list
