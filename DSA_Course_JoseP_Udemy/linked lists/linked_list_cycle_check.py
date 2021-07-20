class Node():
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
def cycle_check(node):
    marker1 = node
    marker2 = node
    
    while marker2 != None and marker2.next != None:
        
        marker1 = marker1.next
        marker2 = marker2.next.next
        
        if marker1 == marker2:
            print(marker1.value)
            return True
    
    return False

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = b

print(cycle_check(a))