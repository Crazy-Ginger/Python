#!/usr/bin/env python3
import argparse
import os
from datetime import date, datetime
from filecmp import cmp
from shutil import copy2, disk_usage, move, rmtree

# checks there is enough space on the disk to duplicate all the images into a tree
dFree = disk_usage("/").free
dUsed = sum(d.stat().st_size for d in os.scandir() if d.is_file())
if dFree <= dUsed:
    raise OSError("Disk too full to perform this operation")

# parses arguments passed to program such as whether to copy or if a source and output file has been set
parser = argparse.ArgumentParser()
parser.add_argument("--copy", "-c", help="set the program to copy files instead of move", action="store_true")
parser.add_argument("--delete", "-d", help="delete files from source if they are found in the output folder", action="store_true")
parser.add_argument("--source", "-s", help="set the source directory")
parser.add_argument("--output", "-o", help="set the output directory")
parser.add_argument("--no-log", "-l", help="turn off the logging function", action="store_true")
args = parser.parse_args()

# if source is passed as arg sets that, else uses some predefined defaults (dependant on os)
if args.source:
    origin_path = args.source
else:
    if os.name == "posix":
        origin_path = os.path.expanduser("~")+"/Pictures/dump"
    elif os.name == "nt":
        origin_path = "D:/Pictures/SD_BackUp/Dump"
os.chdir(origin_path)

if args.output:
    dest_path = args.output
else:
    dest_path = "../Photos"

if os.path.isdir(dest_path) == False:
    os.mkdir(dest_path)
    # used to delete the pre-existing file structure with the sorted photos(?), now it should just add ones that don't alread exist
    # rmtree(dir_Name, True)


months = ["01-Jan", "02-Feb", "03-Mar", "04-Apr", "05-May", "06-Jun", "07-Jul",
          "08-Aug", "09-Sep", "10-Oct", "11-Nov", "12-Dec"]

log = ""
test_itter = 0
# iterates over all files in the directory collecting datestamps and placing them into directories of those dates
for file_Name in os.listdir():
    test_itter += 1
    if (not file_Name.endswith(".JPG")) and (not file_Name.endswith(".CR2")):
        log += "Skipping over " + file_Name + "\n"
        continue

    file_Year = datetime.fromtimestamp(os.path.getmtime(file_Name)).strftime('%Y')
    file_Month = months[int(datetime.fromtimestamp(os.path.getmtime(file_Name)).strftime('%m'))-1]
    file_Date = datetime.fromtimestamp(os.path.getmtime(file_Name)).strftime('%d')

    # checks if the file under that name exists, if it is not the same moves the file with an appendix, otherwise skips
    appendix = ""
    toCopy = True
    deleted = False
    final_dest = file_Year + "/" + file_Month + "/" + file_Date
    while (os.path.isfile(dest_path + "/" + final_dest + "/" + file_Name + appendix) == True):
        if os.path.getsize(file_Name) == os.path.getsize(dest_path + "/" + final_dest + "/" + file_Name + appendix):
            if cmp(file_Name, dest_path + "/" + final_dest + "/" + file_Name + appendix) == True:
                deleted = True
                break

        if appendix == "":
            appendix = "_1"
        elif appendix[1] == "9":
            log += "To many duplicates of: " + str(origin_path) + str(file_Name) + "\n"
            toCopy = False
            break
        else:
            log += "File: " + str(origin_path) + "/" + str(file_Name) + "had same name as " + str(dest_path) +"/"+str(file_Name) +"\n"
            appendix = "_" + str(int(appendix[1])+1)

    if args.delete and deleted == True:
        log += "Duplicate: " + str(origin_path) + str(file_Name) + " was deleted\n"
        os.remove(file_Name)
        continue
    elif toCopy == False:
        log += "File: " + str(origin_path) + str(file_Name) + " was a not moved/saved\n"
        continue

    # creates the year, month & date directories if they don't already exist
    if os.path.isdir(dest_path + "/" + file_Year) == False:
        os.mkdir(dest_path +"/" + file_Year)
    if os.path.isdir(dest_path + "/" + file_Year + "/" + file_Month) == False:
        os.mkdir(dest_path + "/" + file_Year + "/" + file_Month)
    if os.path.isdir(dest_path + "/" + file_Year + "/" + file_Month + "/" + file_Date) == False:
        os.mkdir(dest_path + "/" + file_Year + "/" + file_Month + "/" + file_Date)

    if args.copy:
        copy2(file_Name, dest_path + "/" + final_dest + "/" + file_Name + appendix)
        log += "Copied " + file_Name + "as: " + dest_path + final_dest + file_Name + appendix +"\n"
    else:
        move(file_Name, dest_path + "/" +  final_dest + "/" + file_Name + appendix + "\n"
        log += "Moved " + str(file_Name) + "to: " + str(dest_path)  + str(final_dest) + str(file_Name) + str(appendix) + "\n"

if os.path.isfile(dest_path + "/log.txt"):
    logger = open(dest_path + "/log.txt", "a+")
else:
    logger = open(dest_path + "/log.txt", "w+")
logger.write("Update: " + str(date.today()) + "\n")
logger.write(log + "\n\n")
logger.close()
