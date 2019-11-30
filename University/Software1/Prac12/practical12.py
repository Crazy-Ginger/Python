#!/usr/bin/env python3

def wildcard_pattern(card, l= 0):
    print (l, card)
    if "?" not in card:
        return [card, card]
    elif card[0] == "?":
        return ["0"+ wildcard_pattern(card[1:], l+1)[0], "1" + wildcard_pattern(card[1:], l+1)[1]]


#wildcard_pattern("word")
print (wildcard_pattern("?01010"))

print (wildcard_pattern("??1010"))
