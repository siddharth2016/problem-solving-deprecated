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