import time, datetime
hour = int(time.strftime("%H"))
minu = int(time.strftime("%M"))
sec = int(time.strftime("%S"))
while hour != 21 and minu != 35 and sec != 30:
    print (hour, ":", minu, ":", sec)
    hour = int(time.strftime("%H"))
    minu = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
print ("Done")
print (hour, ":", minu, ":", sec)
