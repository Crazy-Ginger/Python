#!/usr/bin/env python3

def wildcard_pattern(card, pat):
    words = []
    if len(card) == 0:
        return ''
    elif pat not in card:
        return card
    for i in range(len(card)):
        if card[i] == pat and len(words) == 0:
            words.append("0")
            words.append("1")
        elif card[i] == pat:
            words = __caller(words)

        else:
            for j in range(len(words)):
                words[j] += card[i]
        # print (i, words)
    words = sorted(words)
    # print ("\n\n")
    return words

def __caller(words):
    n_words = []
    alter = True
    for i in range(len(words)*2):
        if alter:
            alter = False
            n_words.append(words[i//2] + "1")
        else:
            alter = True
            n_words.append(words[i//2] + "0")

    return n_words

# print (wildcard_pattern("?01010"))
# print (wildcard_pattern("??0101"))
# print (wildcard_pattern("???"))
