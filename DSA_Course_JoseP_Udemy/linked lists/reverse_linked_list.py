class Node():
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
def reverse(node):
    prev = None
    while node != None:
        nextNode = node.next 
        node.next = prev
        prev = node
        node = nextNode

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

reverse(a)

print(d.next.value, c.next.value, b.next.value)
        
        