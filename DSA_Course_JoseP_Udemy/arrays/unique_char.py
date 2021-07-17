def uniq_char(s):
    return len(set(s)) == len(s)

def uniq_char2(s):
    chars = set()
    for v in s:
        if v in chars:
            return False
        chars.add(v)
    return True

print(uniq_char("abcde"))
print(uniq_char("aabcde"))

print("#########")

print(uniq_char2("abcde"))
print(uniq_char2("aabcde"))