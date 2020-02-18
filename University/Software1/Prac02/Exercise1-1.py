## 1
sent = str(input())
if len(sent) == 0:
    sent = "All work and no play makes Jack a dull boy"

words = list()
temp_word = ""
for i in range(0, len(sent)+1):
    char = sent[i:i+1]
    if char == " " or i == len(sent):
        words.append(temp_word)
        temp_word = ""
    else:
        temp_word += char

sent = ""
for i in range(0, len(words)):
    sent += words[i] + " "

print (sent)
