def string_save(string, filename):
    filename = str(filename)
    file = open(filename, 'w')
    file.write(string)
    file.close()

def save_list2file(sentences, filename):
    file = open(filename, 'w')
    for sent in sentences:
        file.write(sent)
    file.close()

def save_to_log(entry, logfile):
    file= open(logfile, 'a')
    file.write("\n"+entry)
    file.close()

def upper_out(filename):
    file = open(filename, 'r')
    output = ""
    for line in file:
        output += line.upper()
    print (output)
    file.close()

def to_upper_case(input_file, output_file):
    in_file = open(input_file, 'r')
    out_file = open(output_file, 'w')
    for line in in_file:
        out_file.write(str(line).upper())
    in_file.close()
    out_file.close()
    
def sum_file(filename):
    ### doesn't work with numbers >9 as haven't implemented it correctly
    file = open(filename, 'r')
    total = 0
    for line in file:
        for char in line:
            try:
                total += int(char)
            except:
                print ("invalid char")
    file.close()
    return total

def save_user_data(filename, user_dict):
    file = open(filename, 'r')
    writer = ""
    for key, val_list in user_dict.items():
        writer += key + ":"
        print (val_list)
    file.close()