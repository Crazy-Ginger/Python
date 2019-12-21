#!/usr/bin/env python3

def detect_correct(word):
    if not isinstance(word, str):
        raise TypeError
    elif len(word) % 3 != 0:
        raise ValueError

    
