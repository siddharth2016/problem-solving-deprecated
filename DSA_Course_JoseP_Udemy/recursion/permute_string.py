def permute(st):
    out = []
    if len(st)==1:
        out = [st]
    else:
        for i, let in enumerate(st):
            for perm in permute(st[:i] + st[i+1:]):
                out += [let + perm]
    return out

print(permute("abc"))
print(permute("siddharth"))
print(permute("ibi"))