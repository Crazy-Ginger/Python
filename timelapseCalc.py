from math import floor as floor
import datetime
def time(nowOrNot = True):
    if nowOrNot:
        currentDT = datetime.datetime.now()
        sHour = int(currentDT.hour)
        sMin = int(currentDT.minute)
    else:
        start = str(input("enter start time: "))
        sHour = int(start[:2])
        sMin = int(start[2:4])
    ######################
    stop = str(input("enter end time: "))
    eHour = int(stop[:2])
    eMin = int(stop[2:4])
    time = 0
    #######################
    if eHour < sHour:
        time = time + eHour*60 + (24 - sHour - 1)*60
    else:
        #print("running else")
        time = (eHour - sHour)*60
    #######################print(time)
    if sMin != 0:
        time = time + eMin + (60-sMin)
    else:
       time = time + eMin 
    #######################
    print ("time = ",time)
    print (floor(time/60), " hours and ", time%60, " minutes")
#____________________________________________________________#
choice = str(input("Is the start time now? ")).upper()
if choice=="Y" or choice=="YES":
    time(True)
else:
    time(False)
