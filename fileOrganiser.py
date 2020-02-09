#!/usr/bin/env python3
from datetime import datetime
import os
from shutil import rmtree, disk_usage, copyfile
from sys import platform


# checks there is enough space on the disk to duplicate all the images into a tree
dFree = disk_usage("/").free
if platform == "linux":
    path = os.path.expanduser("~")+"/Pictures/dump"
elif platform == "win32":
    path = "C:/Photos"

    
os.chdir(path)
dUsed = sum(d.stat().st_size for d in os.scandir() if d.is_file())
if dFree <= dUsed:
    raise OSError("Disk too full to perform this operation")

if os.path.isdir("tmp") == True:
    rmtree("tmp", True)
dirN = "tmp"
os.mkdir(dirN)
months = ["01-Jan", "02-Feb", "03-Mar", "04-Apr", "05-May", "06-Jun", "07-Jul",
          "08-Aug", "09-Sep", "10-Oct", "11-Nov", "12-Dec"]

# iterates over all files in the directory collecting datestamps
for fName in os.listdir():
    if fName.endswith(".JPG") or fName.endswith(".CR2") or fName.endswith(".MOV"):
        fYear = datetime.fromtimestamp(os.path.getmtime(fName)).strftime('%Y')
        fMonth = months[int(datetime.fromtimestamp(os.path.getmtime(fName)).strftime('%m'))-1]
        fDate = datetime.fromtimestamp(os.path.getmtime(fName)).strftime('%d')
        
        if os.path.isdir("tmp/"+fYear) == False:
            os.mkdir("tmp/"+fYear)
        if os.path.isdir("tmp/"+fYear+"/"+fMonth) == False:
            os.mkdir("tmp/"+fYear+"/"+fMonth)
        if os.path.isdir("tmp/"+fYear+"/"+fMonth+"/"+fDate) == False:
            os.mkdir("tmp/"+fYear+"/"+fMonth+"/"+fDate)
        copyfile(fName, "tmp/"+fYear+"/"+fMonth+"/"+fDate+"/"+fName)

