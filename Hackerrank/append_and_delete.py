c = 0
s = input()
t = input()
k = int(input())
l = len(s)
for i, j in zip(s, t):
    if i!=j:
        break
    c += 1

if k%2 == (len(s)+len(t))%2:
    vmin = len(s) + len(t) - 2*c
else:
    vmin = len(s) + len(t) + 1

if k < vmin:
    print("No")
else:
    print("Yes")
