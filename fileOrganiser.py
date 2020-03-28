#!/usr/bin/env python3
from datetime import datetime
from filecmp import cmp
from shutil import rmtree, disk_usage, move, copy2
import os, argparse


# checks there is enough space on the disk to duplicate all the images into a tree
dFree = disk_usage("/").free
dUsed = sum(d.stat().st_size for d in os.scandir() if d.is_file())
if dFree <= dUsed:
    raise OSError("Disk too full to perform this operation")

# parses arguments passed to program such as whether to copy or if a source and destination file has been set
parser = argparse.ArgumentParser()
parser.add_argument("--copy", "-c", help="set the program to copy files instead of move", action="store_true")
parser.add_argument("--origin", "-o", help="set the origin directory")
parser.add_argument("--destination", "-d", help="set the destination directory")
parser.add_argument("--no-log", "-l", help="turn off the logging function", action="store_true")
args = parser.parse_args()

# if origin is passed as arg sets that, else uses some predefined defaults (dependant on os)
if args.origin:
    origin_path = args.origin
else:
    if os.name == "posix":
        origin_path = os.path.expanduser("~")+"/Pictures/dump"
    elif os.name == "nt":
        origin_path = "D:/Pictures/SD_BackUp/Dump"
os.chdir(origin_path)

if args.destination:
    destination_path = args.destination
else:
    destination_path = "../Photos"

if os.path.isdir(destination_path) == False:
    os.mkdir(destination_path)
    # used to delete the pre-existing file structure with the sorted photos(?), now it should just add ones that don't alread exist
    # rmtree(dir_Name, True)


months = ["01-Jan", "02-Feb", "03-Mar", "04-Apr", "05-May", "06-Jun", "07-Jul",
          "08-Aug", "09-Sep", "10-Oct", "11-Nov", "12-Dec"]

strange_log = ""
# iterates over all files in the directory collecting datestamps and placing them into directories of those dates
for file_Name in os.listdir():
    if not fName.endswith(".JPG") or not fName.endswith(".CR2") or not fName.endswith(".MOV"):
        continue
    file_Year = datetime.fromtimestamp(os.path.getmtime(fName)).strftime('%Y')
    file_Month = months[int(datetime.fromtimestamp(os.path.getmtime(fName)).strftime('%m'))-1]
    file_Date = datetime.fromtimestamp(os.path.getmtime(fName)).strftime('%d')

    # checks if the file under that name exists, if it is not the same moves the file with an appendix, otherwise skips
    appendix = ""
    if os.path.isfile(destination) == True:
        if os.path.getsize(origin) == os.path.getsize(destination):
            if cmp(fName, destination) == True:
                #add code

    # creates the year, month & date directories if they don't already exist
    if os.path.isdir(dir_Name +"/"+file_Year) == False:
        os.mkdir(dir_Name +"/"+file_Year)
    if os.path.isdir(dir_Name +"/"+file_Year+"/"+file_Month) == False:
        os.mkdir(dir_Name +"/"+file_Year+"/"+file_Month)
    if os.path.isdir(dir_Name +"/"+file_Year+"/"+file_Month+"/"+file_Date) == False:
        os.mkdir(dir_Name +"/"+file_Year+"/"+file_Month+"/"+file_Date)

    if args.copy:
        copy2(file_Name, dest_File + file_Name + appendix)
    else:
        move(file_Name, dest_File +"/" + file_Year + "/" + file_Month + "/" + file_Date + "/" + file_Name + appendix)
