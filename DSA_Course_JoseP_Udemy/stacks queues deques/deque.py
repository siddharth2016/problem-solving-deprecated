class Deque():
    
    def __init__(self):
        self.deque = []
        
    def size(self):
        return len(self.deque)
    
    def isEmpty(self):
        return self.deque == []
    
    def addFront(self, item):
        self.deque.insert(0, item)
        
    def removeFront(self):
        return self.deque.pop(0)
    
    def addRear(self, item):
        self.deque.append(item)
        
    def removeRear(self):
        return self.deque.pop()
    
dq = Deque()
print(dq.isEmpty(), dq.size())
dq.addFront(1)
dq.addFront(2)
dq.addFront(3)
print(dq.removeRear(), dq.removeRear(), dq.removeRear())

print(dq.isEmpty(), dq.size())
dq.addRear(1)
dq.addRear(2)
dq.addRear(3)
print(dq.removeFront(), dq.removeFront(), dq.removeFront())
