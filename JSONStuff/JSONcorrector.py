import os

rootdir = "D:/Matty's Data/"
rfile = "Facebook_messages.txt"
os.chdir(rootdir)
wfile = "Output.txt"
prevLine = ""

with open (rfile, "r") as rf, open (wfile, "w") as wf:
    for line in rf:
        if (line[0] != "[" and line[0] !="{" and line[0] !='"' and line[0] !="}" and line[0] !="]"):
            prevLine = prevLine.rstrip()
        wf.write(prevLine)
        prevLine = line
    wf.write(line)
