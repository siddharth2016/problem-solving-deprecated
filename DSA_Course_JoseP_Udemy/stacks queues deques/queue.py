class Queue():
    
    def __init__(self):
        self.queue = []
    
    def size(self):
        return len(self.queue)
    
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        return self.queue.pop(0)
    
    def isEmpty(self):
        return self.queue == []
    
q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue(), q.dequeue(), q.dequeue())
print(q.size())