def find_common_keys(dict1,dict2):
    return list(set(dict1.keys() & set(dict2.keys())))

dict1={"a":1,"b":2}
dict2={"A":3,"B":4}

print(find_common_keys(dict1,dict2))
