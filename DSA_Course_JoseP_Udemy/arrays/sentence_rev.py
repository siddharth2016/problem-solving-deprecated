def reverse_sentence(stc):
    stack = []
    dummy = ""
    for val in stc + " ":
        if val == " ":
            if dummy != "":
                stack.append(dummy)
            dummy = ""
        else:
            dummy+=val
    res = ""
    for val in stack[::-1]:
        res += val + " "
    return res.rstrip()

print(reverse_sentence("   hello world scala python dsa course"))
print(reverse_sentence("Hello World  Scala python dsa "))