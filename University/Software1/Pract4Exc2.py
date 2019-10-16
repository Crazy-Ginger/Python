int_str = input("Your list of numbers: ")
int_list = []
temp_str = ""
for char in int_str:
    if char != " ":
        temp_str += char
    elif char == " ":
        int_list.append(int(temp_str))
        temp_str = ""
int_list.append(int(temp_str))

even_int = []
for i in int_list:
    if i % 2 == 0:
        even_int.append(i)


print ("int_list: ", int_list)
print ("even_int: ", even_int)
