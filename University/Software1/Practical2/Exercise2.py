imp_unit = input("What are you converting:")
imp_unit = imp_unit.lower()

imp_value = float(input("How much of that thing:"))

##distances all using approximates of the constants used to between them, all rounded to 4 dp
if imp_unit =="miles":
    print (round(imp_value*1.60934, 4), "km or", round(imp_value*1.60934721*1000, 4), "m")
elif imp_unit =="inches":
    print (round((imp_value*0.0254)/1000, 4), "km or", round(imp_value*0.0254,4), "m")
elif imp_unit =="yards":
    print (round((imp_value/1.0936)/1000, 4), "km or", round(imp_value/1.0936, 4), "m")
elif imp_unit =="feet"or imp_unit =="foot":
    print (round((imp_value*0.3048)/1000, 4), "km or", round(imp_value*0.3048, 4), "m")

## weights all using approximates 
elif imp_unit =="ounce"or imp_unit =="oz":
    print (round((imp_value*28.349523125)/1000, 4), "kg or", round((imp_value*28.349523125), 4), "g")
elif imp_unit =="pound"or imp_unit =="lb":
    print (round(imp_value*0.45359237, 4), "kg or", round(imp_value*0.45359237*1000, 4), "g")
elif imp_unit =="stone"or imp_unit =="st":
    print (round(imp_value*6.35029318, 4), "kg or", round(imp_value*6.35029318*1000, 4), "g")

##volumes
elif imp_unit == "fluid ounce":
    print(round(imp_value*28.4130625*1000, 4), "L or", round(imp_value*28.4130625, 4), "mL")
elif imp_unit == "pint":
    print (round(imp_value*568.26125*1000, 4), "L or", round(imp_value*568.26125, 4), "mL")
elif imp_unit == "gallon":
    print (round(imp_value*4.54609, 4), "L or", round((imp_vaule*4.54609)/1000, 4), "mL")

##error collector
else:
    print ("Error")
    exit()
