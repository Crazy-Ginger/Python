import os

rootdir = "D:/Matty's Data/"
rfile = "Facebook_messages.txt"
os.chdir(rootdir)

iterator = 0
firstChars = ["[", "{", "}", "]"]
with open (rfile, "r") as rf:
    for line in rf:
        if line[0] not in firstChars:
            firstChars.append(line[0])
            print ("line: " , iterator)
            print ("char: ", line[0])
            print()
        iterator += 1
