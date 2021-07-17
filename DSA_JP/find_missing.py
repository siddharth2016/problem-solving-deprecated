from collections import defaultdict

def find(arr1, arr2):
    
    finder = defaultdict(lambda: 0)
    
    for v in arr2:
        finder[v] += 1
    
    for v in arr1:
        if finder[v] == 0:
            return v
        finder[v]-=1

print(find([5, 5, 7, 7], [5, 7, 7]))

def find2(arr1, arr2):
    res = 0
    for x in arr1+arr2:
        res^=x
    return res

print(find2([1, 2, 3, 5,5,7,7], [1, 2, 3, 5,7,7]))