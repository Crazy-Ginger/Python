from decimal import *
total = 0
#sets the number of decimal places for floats to 100
getcontext().prec = 100

for i in range(1, 100):
    numb = str(Decimal(i).sqrt())
    cont = False
    
    for char in numb:
        if char == '.':
            cont = True
            break
    #print(i)   
        #print (numb)
    if cont == True:
        for char in reversed(numb):
            if char != '.':
                total += int(char)
            else:
                break
    print ("i: ", i , "\ttotal: ", total)       
print(total)
