def reverse(st):
    if len(st)>0:
        return st[-1] + reverse(st[:-1])
    return ""

def reverse2(st):
    if len(st)>0:
        return reverse2(st[1:]) + st[0]
    return ""

print(reverse("hello world"))
print(reverse2("hello world"))