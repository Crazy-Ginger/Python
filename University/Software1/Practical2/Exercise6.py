side1 = float(input("Side 1: "))
side2 = float(input("Side 2: "))
side3 = float(input("Side 3: "))

semi_per = (side1+side2+side3)/2

inter_value = semi_per*(semi_per-side1)*(semi_per-side2)*(semi_per-side3)

area = round(pow(inter_value, 0.5),4)

print ("area:",area)
