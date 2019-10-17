sent = input("enter a sentence: ")
sent = sent.lower()
spaceless_sent = ""
CamelCaseSent = ""
list_sent = []
to_upper = True
temp_str = ""
for char in sent:
    if to_upper:
        CamelCaseSent += char.upper()
        spaceless_sent += char
        temp_str += char.upper()
        to_upper = False
    elif char != " ":
        spaceless_sent += char
        CamelCaseSent += char
        temp_str += char
        to_upper = False
    elif char == " ":
        to_upper = True
        list_sent.append(temp_str)
        temp_str = ""
    else:
        print ("Error at:", char)
        break
list_sent.append(temp_str)
print ("spaceless: ",spaceless_sent)
print ("CamelCase: ", CamelCaseSent)
print ("List_sent: ", list_sent)
