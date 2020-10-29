import os

os.chdir("/mnt/f/")
images = set()
with open("toView.txt", "r") as file:
    line = file.readline()
    while line:
        images.add(line)

file.close()
print(images)
input()
