#!/usr/bin/env python3
from datetime import datetime
from filecmp import cmp
from shutil import rmtree, disk_usage, move
from sys import platform
import os, argparse


# checks there is enough space on the disk to duplicate all the images into a tree
dFree = disk_usage("/").free
dUsed = sum(d.stat().st_size for d in os.scandir() if d.is_file())
if dFree <= dUsed:
    raise OSError("Disk too full to perform this operation")

parser = argparse.ArgumentParser()
parser.parse_args()

if os.name == "posix":
    origin_path = os.path.expanduser("~")+"/Pictures/dump"
elif platform == "win32":
    origin_path = "D:/Pictures/SD_BackUp/Dump"
os.chdir(origin_path)


dir_Name = "../Photos"
if os.path.isdir(dir_Name) == False:
    os.mkdir(dir_Name)
    # used to delete the pre-existing file structure with the sorted photos(?), now it should just add ones that don't alread exist
    #rmtree(dir_Name, True)


months = ["01-Jan", "02-Feb", "03-Mar", "04-Apr", "05-May", "06-Jun", "07-Jul",
          "08-Aug", "09-Sep", "10-Oct", "11-Nov", "12-Dec"]

strange_log = ""
# iterates over all files in the directory collecting datestamps and placing them into directories of those dates
""" for file_Name in os.listdir():
    if not fName.endswith(".JPG") or not fName.endswith(".CR2") or not fName.endswith(".MOV"):
        continue
    file_Year = datetime.fromtimestamp(os.path.getmtime(fName)).strftime('%Y')
    file_Month = months[int(datetime.fromtimestamp(os.path.getmtime(fName)).strftime('%m'))-1]
    file_Date = datetime.fromtimestamp(os.path.getmtime(fName)).strftime('%d')
    
    appendix = ""
    origin = path + file_Name
    destination = dir_Name +"/"+file_Year+"/"+file_Month+"/"+file_Date+"/"+ file_Name

    if os.path.isfile(destination) == True:
        if os.path.getsize(origin) == os.path.getsize(destination):
            if cmp(fName, destination) == True:
                break

    
    if os.path.isdir(dir_Name +"/"+file_Year) == False:
        os.mkdir(dir_Name +"/"+file_Year)
    if os.path.isdir(dir_Name +"/"+file_Year+"/"+file_Month) == False:
        os.mkdir(dir_Name +"/"+file_Year+"/"+file_Month)
    if os.path.isdir(dir_Name +"/"+file_Year+"/"+file_Month+"/"+file_Date) == False:
        os.mkdir(dir_Name +"/"+file_Year+"/"+file_Month+"/"+file_Date)

    move(fName, dir_Name +"/"+file_Year+"/"+file_Month+"/"+file_Date+"/"+fName) """