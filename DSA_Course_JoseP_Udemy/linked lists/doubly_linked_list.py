class DoublyLinkedListNode():
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next = b
b.prev = a

b.next = c
c.prev = b

temp = a

while temp != None:
    print(temp.value)
    temp = temp.next
