#!/usr/bin/env python3

def to_barcode(binary):
    printer = ""
    for i in binary:
        if i == "1":
            printer += "|"
        elif i == "0":
            printer += "."
        else:
            return None
    return printer
