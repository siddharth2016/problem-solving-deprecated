class Stack2Queue():
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, item):
        self.stack1.append(item)
    
    def dequeue(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
q = Stack2Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.stack1, q.stack2)
print(q.dequeue())
q.enqueue(4)
print(q.dequeue(), q.dequeue(), q.dequeue())