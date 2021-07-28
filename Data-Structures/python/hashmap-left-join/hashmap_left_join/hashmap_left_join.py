hash1={'fond': 'enamored','wrath': 'anger','diligent': 'employed','outfit':'grab','guide':'usher' }
hash2={'fond': 'averse','wrath': 'diligent','diligent': 'idle','guide':'follow','flow':'jam' }

def left_join(hash1,hash2):
    newArr=[]
    for i, v in enumerate(hash1):
    
        newArr+=[[v]]
        newArr[i].append(hash1[v])
        if v in hash2:
            newArr[i].append(hash2[v])
        else:
            newArr[i].append(None)
                       
    return newArr


print(left_join(hash1,hash2))











