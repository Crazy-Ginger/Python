def get_file(filename):
    value_dict = {}
    file = open(filename, 'r')
    for line in file:
        if line[0] == '#':
            continue
        key = ""
        for i in range(len(line)):
            key += line[i]
            if line[i] == ',':
                value = line[i+1:]
                break
        value_dict[key] = float(value)
    return value_dict

def min_Precipitation(value_dict):
    min_key = list(value_dict.keys())[0]
    min_val= value_dict[min_key]
    for key,value in value_dict.items():
        if value < min_val:
            min_val = value
            min_key = key
    return min_key, min_val

def max_Precipitation(value_dict):
    max_key = list(value_dict.keys())[0]
    max_val= value_dict[max_key]
    for key,value in value_dict.items():
        if value > max_val:
            max_val = value
            max_key = key
    return max_key, max_val
    
def average_Precipitation(value_dict):
    total = 0.0
    size = 0
    for val in value_dict.values():
        total += val
        size += 1
    return round(total/size,2)
