def check_anagram(s1, s2):   
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for val in s1:
        if val not in count:
            count[val] = 0
        count[val]+=1
    
    for val in s2:
        if val not in count:
            return False
        count[val] -= 1
        
    for value in count.values():
        if value!=0:
            return False
    return True

print(check_anagram("publiic relations", "crap built on lies"))