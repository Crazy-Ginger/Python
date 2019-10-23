#exec2
def get_words_starting_with(text, letter):
    text = str(text).lower()
    letter = letter.lower()
    words = text.split()
    begin_with = []
    
    for word in words:
        if letter == word[:(len(letter))]:
            begin_with.append(word)
    return begin_with

#exec3
def words_starting_noRep(text, letter):
    text = str(text).lower()
    letter = letter.lower()
    words = text.split()
    begin_with = []
    
    for word in words:
        if letter == word[:(len(letter))] and word not in begin_with:
            begin_with.append(word)
    return begin_with


#exec5
def caesar_encrypt(text, offset):
    text = str(text).lower()
    
