import clr
from time import sleep
clr.AddReference('OpenHardwareMonitor')
from OpenHardwareMonitor.Hardware import Computer

c = Computer()
c.CPUEnabled = True # get the Info about CPU
c.GPUEnabled = True # get the Info about GPU
c.Open()
while True:
    for hard in c.Hardware:
        print (hard, "\t", hard.Name)
    # print (c.Hardware[0])
    c.Hardware[0].Update()

    #for a in range(0, len(c.Hardware[0].Sensors)):
    #print(c.Hardware[0].Sensors[a].Identifier)
    # if "/intelcpu/0/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
    #    print(c.Hardware[0].Sensors[a].get_Value())
    #c.Hardware[0].Update()
