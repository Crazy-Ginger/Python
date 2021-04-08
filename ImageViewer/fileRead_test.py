import os

os.chdir("D:\\Photos\\TheySay1980")
viewed_file = open("viewed.txt")
viewed = []
to_view = []
for line in viewed_file:
    viewed.append(line)
print("viewed:", viewed)
counter = 0
added_counter = 0
for path, subdirs, files in os.walk(os.getcwd()):
    for name in files:
        counter += 1
        if not name.lower().endswith(".jpg") and not name.lower().endswith(".png"):
            break
        added_counter += 1
        file = os.path.join(path, name)
        if file not in viewed:
            to_view.append(file)
# print("to_view:", to_view)
print(len(to_view))
print(to_view[-10])
print("counter: ", counter)
print("added_counter", added_counter)
