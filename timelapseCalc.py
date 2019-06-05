from math import floor as floor
start = str(input("enter start time: "))
stop = str(input("enter end time: "))

sHour = int(start[:2])
sMin = int(start[2:4])

eHour = int(stop[:2])
eMin = int(stop[2:4])

time = 0

if eHour < sHour:
    time = time + eHour*60 + (24-sHour-1)*60
    #print ((24-sHour)*60)
    #print (eHour*60)
    #print (time)
    
else:
    #print("running else")
    time = (eHour - sHour)*60

    
#print(time)
time = time + eMin + (60-sMin)

print ("time = ",time)
print (floor(time/60), " hours and ", time%60, " minutes")
