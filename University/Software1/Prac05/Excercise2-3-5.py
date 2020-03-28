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
    offset = int(offset)
    cypher = ""
    for char in text:
        if char == " ":
            cypher += " "
        else:
            cypher += chr((((ord(char)+offset)-97)%26) +97)
    return cypher

def caesar_decrypt(text, offset):
    text = str(text).lower()
    offset = int(offset)
    cypher = ""
    for char in text:
        if char == " ":
            cypher += " "
        else:
            cypher += chr((((ord(char)-offset)-97)%26) +97)
    return cypher

def decrypter(text):
    text = str(text).lower()
    decrypted = []
    for i in range(1, 26):
        check_cypher = ""
        for char in text:
            if char == " ":
                check_cypher += " "
            else:
                check_cypher += chr((((ord(char)+i)-97)%26) +97)
        if "the" in check_cypher or "had" in check_cypher == True or "and" in check_cypher == True or "have" in check_cypher == True or "that" in check_cypher == True:
            decrypted.append(check_cypher)
    return decrypted
