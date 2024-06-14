def odd_one(l):

    if type(l[0])==type(l[1]):
        type_me = type(l[0])
    else:
        if type(l[2])==type(l[1]):
            type_me = type(l[2])
        else:
            type_me = type(l[0])
            
    for i in l:
        if type(i) != type_me:
            if type(i) == int:
                return 'int'
            if type(i) == float:
                return 'float'
            if type(i) == str:
                return 'str'
            if type(i) == bool:
                return 'bool'
            
        
        
    
print(odd_one(eval(input().strip())))
