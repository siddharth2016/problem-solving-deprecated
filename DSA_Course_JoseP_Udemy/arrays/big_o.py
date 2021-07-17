def sum1(n):
    return sum(range(n+1))
print(sum1(10)) # O(n)

def sum2(n):
    return (n*(n+1))/2
print(sum2(10)) # O(1)

# Constant O(1)
def func_const(values):
    print(values[0])
func_const([1,2,3])

# Linear O(n)
def func_linear(values):
    for i in values:
        print(i)
func_linear([1,2,3,4,5])

# Quad O(n^2)
def func_quad(values):
    for f in values:
        for s in values:
            print(f, s)
func_quad([1,2,3,4,5])

# Linear O(n)
def func_2(values):
    for i in values:
        print(i)
    for i in values:
        print(i)
func_2([1,2,3,4])

# Sime Comp O(n)
def comp(values):
    
    print(values[0])    #O(n)
    
    mid = len(values)//2
    
    for i in values[:mid]:
        print(i)    #O(n/2)
    
    for i in range(10):
        print("comp")   #O(10)
comp([1,2,3,4,5,6,7,8,9,10])

# Best and Worst Case Complexity
def bestWorst(values, match):
    for val in values:
        if val == match:
            return True     #O(1) if first element matches it, best case
    return False    #O(n)   if no element matches it, worst case
print(bestWorst([1,2,3,4,5,6,7,8,9,10], 1))
print(bestWorst([1,2,3,4,5,6], 7))

# Space O(n)
def spaceN(value):
    l = []
    for i in range(value):
        l.append(i)
    print(l)
spaceN(5)

# Space O(1)
def spaceConst(value):    
    for i in range(value):
        print("Hello Space Const")
spaceConst(10)
