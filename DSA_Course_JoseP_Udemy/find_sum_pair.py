def find_pair(lst, k):
    
    if len(lst)<2:
        return
    
    found = {}
    pairs = 0
    output = set()
    
    for val in lst:
        
        t = k - val
        
        if t in found:
            pairs += found[t]
            output.add((min(t, val), max(t, val)))
        
        if val not in found:
            found[val] = 0
        found[val]+=1
    
    return pairs, output

print(find_pair([1,3,2,2], 4))