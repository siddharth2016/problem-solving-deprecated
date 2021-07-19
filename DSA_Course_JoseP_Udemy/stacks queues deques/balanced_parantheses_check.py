def balance_check(inp):
    balance = []
    open = set(['(','[','{'])
    matches = set([('(',')'), ('[',']'), ('{','}')])
    for br in inp:
        if br in open:
            balance.append(br)
        else:
            if len(balance) == 0:
                return False
            top = balance.pop()
            if (top, br) not in matches:
                return False
    
    return len(balance) == 0

print(balance_check("()"))
print(balance_check("({[]})"))
print(balance_check("()[]{}((()))"))
print(balance_check("()){"))