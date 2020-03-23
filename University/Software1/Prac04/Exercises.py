def sum_digits(numb):
    total = 0
    numb = str(numb)
    for char in numb:
        total += int(char)
    return total

def pairwise_digits(a, b):
    a = str(a)
    b = str(b)
    output = ""
    to_add = abs(len(a) - len(b))
    if len(a) > len(b):
        length = len(b)
    else:
        length = len(a)

    for i in range(length):
        if a[i] == b[i]:
            output += "1"
        else:
            output += "0"

    for i in range(to_add):
        output += "0"

    return output
        
def to_base10(binary):
    binary = str(binary)
    power = len(binary)-1
    denary = 0
    for i in binary:
        denary += int(i)*(2**power)
        power -= 1
    return denary


def floyd_tri(rows):
    rows = int(rows)
    zero = False
    for i in range(1, rows+1):
        printer = ""
        for j in range(i):
            if zero == False:
                printer += "1"
                zero = True
            else:
                printer += "0"
                zero = False
        print (printer)

    
def sum_lists(list_2D):
    #test input
    #data = [[1,2,3], [2], [1, 2, 3, 4]]
    output =[]
    for row in list_2D:
        total = 0
        for val in row:
             total += val
        output.append(total)
    print(output)



## don't go bigger than 100 as the formatting breaks after that
def inc_triangle(rows):
    rows = int(rows)
    numb = 1
    
    for i in range(1, rows+1):
        printer = ""
        for j in range(i):
            if numb < 10:
                printer += " "
            printer += str(numb)+ " "
            numb += 1
        print (printer)


def alphabet_pyra(rows):
    rows = int(rows)
    indenter = rows
    for i in range(1, rows+1):
        for j in range(i):
            print("dick")
