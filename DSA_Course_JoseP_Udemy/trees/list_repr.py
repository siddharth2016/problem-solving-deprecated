def BinaryTree(rootValue):
    return [rootValue, [], []]

def insertLeft(r, leftValue):
    left = r.pop(1)
    
    if len(left) > 1:
        r.insert(1, [leftValue, left, []])
    else:
        r.insert(1, [leftValue, [], []])
    return r

def insertRight(r, rightValue):
    right = r.pop(2)
    
    if len(right) > 1:
        r.insert(2, [rightValue, [], right])
    else:
        r.insert(2, [rightValue, [], []])
    
    return r

test = BinaryTree(1)
insertLeft(test, 7)
insertLeft(test, 4)
insertLeft(test, 2)
insertRight(test[1], 5)
insertRight(test, 3)
insertLeft(test[2], 6)
print(test)