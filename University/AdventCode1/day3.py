#!/usr/bin/env python3

def sizer(vector):
    verticle = 0
    horizontal = 0
    for i in vector:
        if i[0] == "U" or i[0] == "D":
            verticle += int(i[1:])
        elif i[0] == "R" or i[0] == "L":
            horizontal += int(i[1:])
    return [verticle, horizontal]

l1 = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
l2 = ["U62","R66","U55","R34","D71","R55","D58","R83"]

# l1 = ["R98","U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"]
# l2 =["U98","R91,D20,R16,D67,R40,U7,R15,U6,R7"]

print (sizer(l1))
print (sizer(l2))

