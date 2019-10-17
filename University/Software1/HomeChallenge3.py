#!/usr/bin/env python3
def to_binary(numb):
    remainder = int(numb)
    binary = ""
    while remainder > 0:
        binary += str(remainder % 2)
        remainder = remainder // 2
    binary = binary[::-1]
    #print (binary)
    return binary

def eval_poly(poly, x):
    x = int(x)
    total = 0
    for i in range (len(poly)):
        total += poly[i]*(x**i)
    #print (total)
    return total

def add_poly(poly_p, poly_q):
    new_poly = []
    if len(poly_p) >= len(poly_q):
        for i in range (len(poly_q)):
            new_poly.append(poly_p[i]+poly_q[i])
        for i in range (len(poly_q), len(poly_p)):
            new_poly.append(poly_p[i])
    
    elif len(poly_p)< len(poly_q):
        for i in range (len(poly_p)):
            new_poly.append(poly_p[i]+poly_q[i])
        for i in range (len(poly_p), len(poly_q)):
            new_poly.append(poly_q[i])
    return new_poly

def product_poly(poly_p, poly_q):
    new_poly = [0]*(len(poly_p)+len(poly_q)-1)
    
    for i in range (len(poly_q)):
        for j in range (len(poly_p)):
            new_poly[i+j] += poly_p[j]*poly_q[i]
    return new_poly
