#!/usr/bin/env python3

def wildcard_pattern(card, level = 1):
    print (level,":", card)
    if '?' not in card or len(card) < 1:
        print ("exiting at",card)
        return card

    elif card[0] == "?":
        return "0" + wildcard_pattern(card[1:], level +1), "1" + wildcard_pattern(card[1:], level+1)

    else:
        return card[0] + wildcard_pattern(card[1:], level+1)

#wildcard_pattern("word")
wildcard_pattern("?0101?")
