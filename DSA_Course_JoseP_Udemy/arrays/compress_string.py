def compress(stc):
    res = ""
    if len(stc)==0:
        return ""
    curr = stc[0]
    count = 1
    for s in stc[1:]:
        if s != curr:
            res += curr + str(count)
            curr = s
            count = 0
        count+=1
    res += curr + str(count)
    return res

print(compress("AAABBBBCCCDDDD"))
print(compress("aaaabbbbAAAlkdhfladjhfqiwuertgq"))
print(compress("A"))
print(compress(""))