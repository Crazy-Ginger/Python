#!/usr/bin/env python3

def wildcard_pattern(card):
    if '?' not in card:
        return card
    else:
        if card[0] == "?":
            

wildcard_pattern("word")
wildcard_pattern("wor?")
