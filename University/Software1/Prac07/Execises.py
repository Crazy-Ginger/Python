def display_dico(dico):
    if isinstance(dico, dict) == True:
        for key, val in dico.items():
            print(key, "-->", val)
    else:
        return None

def concat_dico(dico1, dico2):
    new_dico = {}
    for key, val in dico1.items():
        new_dico[key] = val

    for key, val in dico2.item
        if key in new_dico:
            temp = []
            temp.append(new_dico[key])
            temp.append(dico2[key])
            new_dico[key] = temp
        
        else:
            new_dico[key] = val
    return new_dico

def map_list(keys, values):
    if len(keys) != len(values):
        print ("Error: length difference between keys and values")
        return None

    new_dico = {}
    for i in range(len(keys)):
        if keys[i] in new_dico:
            print ("Error: duplicate keys")
            return None
        new_dico[keys[i]] = values[i]
    return new_dico

def reverse_dict(dico):
    new_dico = {}
    for  key, val in dico.items():
        if val in new_dico:
            print ("Error duplicate values")
            return None
        new_dico[val] = key
    return new_dico
