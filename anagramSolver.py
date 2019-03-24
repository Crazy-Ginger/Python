anagram = str(input("Anagram to solve: "))
choice = str(input("True solution? "))
anagramchars = list()

for char in anagram:
    anagramchars.append(char)
    
wordlist = list()

with open("C:\Coding\Word_list.txt", "r") as file:
    for line in file:
        if (len(line) <= len(anagram)+1):
            line = line.replace("\n", "")
            wordlist.append(line)

if choice == "y" or choice == "Yes" or choice == "yes":
    for word in wordlist:
        if len(word) == len(anagram):
            if sorted(word) != sorted(anagram):
                wordlist.remove(word)
        else:
            wordlist.remove(word)
    if len(word) > 0:
        for word in wordlist:
            print (word)
    else:
        print ("Sorry no solutions")
else:
    
