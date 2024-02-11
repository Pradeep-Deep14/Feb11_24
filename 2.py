def find_common_keys(dict1,dict2):
    return list(set(dict1.keys() & set(dict2.keys())))

dict1={"a":1,"b":2,"c":3}
dict2={"b":5,"c":6,"d":7}

print(find_common_keys(dict1,dict2))

