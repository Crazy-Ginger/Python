def get_file(filename):
    value_dict = {}
    file = open(filename, 'r')
    for line in file:
        if line[0] == '#' or line[0]=='!':
            continue
        line = line.rstrip().split(',')
        key = line[0] + "-" + line[1]
        vals = line[2:]
        for i in range(len(vals)):
            vals[i] = float(vals[i])
        value_dict[key] = vals
    return value_dict

def get_totals(dict_val):
    new_dict = {}
    for key, val in dict_val.items():
        
    
def out_file(filename, dict_val):
    file = open(filename+".csv", "w")
    
