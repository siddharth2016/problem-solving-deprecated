class Node():
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
def nth_to_last_node(n, node):
    fast = node
    slow = node
    count = 1
    while count<n:
        fast = fast.next
        count+=1
    
    while fast.next!=None:
        slow = slow.next
        fast = fast.next
    
    return slow.value

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

print(nth_to_last_node(2, a))