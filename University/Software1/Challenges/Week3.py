#!/usr/bin/env python3
def to_binary(numb):
    remainder = int(numb)
    binary = ""
    while remainder > 0:
        binary += str(remainder % 2)
        remainder = remainder // 2
    binary = binary[::-1]
    return binary

def eval_poly(poly, x):
    x = int(x)
    total = 0
    for i in range (len(poly)):
        total += poly[i]*(x**i)
    return total


def add_poly(poly_p, poly_q):
    new_poly = []
    #If statement to check whick poly is longer to avoid an out of range exception
    if len(poly_p) >= len(poly_q):
        shortest = len(poly_q)
        longest = len(poly_p)
        long_poly = poly_p
    elif len(poly_p)< len(poly_q):
        shortest = len(poly_p)
        longest = len(poly_q)
        long_poly = poly_q
    
    for i in range (shortest):
        new_poly.append(poly_p[i]+poly_q[i])
    for i in range (shortest, longest):
        new_poly.append(long_poly[i])
    return new_poly

def product_poly(poly_p, poly_q):
    new_poly = [0]*(len(poly_p)+len(poly_q)-1)
    
    for i in range (len(poly_q)):
        for j in range (len(poly_p)):
            new_poly[i+j] += poly_p[j]*poly_q[i]
    return new_poly

def to_latex(poly):
    out_poly = ""
    incrementor = len(poly)-1
    for i in poly:
        if incrementor == 0:
            out_poly += str(i)
        elif incrementor == 1:
            out_poly += str(i) + "x+"
        else:
            out_poly += str(i) + "x" + "^{" + str(incrementor) + "}+"
        incrementor -= 1
    return out_poly
    
