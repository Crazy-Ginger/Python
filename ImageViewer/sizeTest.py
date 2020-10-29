import os

os.chdir("D:/Photos")
images = set()
with open("toView.txt", "r") as file:
    line = file.readline()
    while line:
        images.add(line)

file.close()
print(images)
input()
