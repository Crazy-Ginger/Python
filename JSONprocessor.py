from IPython.core.debugger import set_trace
import json
import os

def datacompile():
    alldata = []
    rootdir = "E:/Matty's Data/Facebook/messages"
    for subdir, dirs, files in os.walk(rootdir):
        files = [os.path.join(subdir, f) for f in files if f.endswith(".json")]
        for file in files:
            #print (os.path.join(subdir," ", file))
        
            with open(file, "r") as current_file:
                current_data = json.load(current_file)
                alldata.append(str(current_data))
                #print(current_data)
                #cont = input("\n stop me")


    with open("E:/Matty's Data/Facebook_messages.json", 'w') as comp:
        json.dump(alldata, comp)
    print("File write complete")

datacompile()
