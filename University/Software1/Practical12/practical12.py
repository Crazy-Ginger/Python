#!/usr/bin/env python3

def __upside_down(char):
    if char != "?":
        return char
    else:
        return "1"

def wildcard_pattern(card):
    string = []
    if '?' not in card:
        return card
    else:
        for i in range(len(card)):
            if card[i] == "?":
                

            
            

wildcard_pattern("word")
wildcard_pattern("wor?")
