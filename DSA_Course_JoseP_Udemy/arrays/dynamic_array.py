# import sys
# d = []

# for i in range(10):
    
#     print("Length of array {0:3d}, Size of array {1:4d}".format(i, sys.getsizeof(d)))
#     d.append(i)

import ctypes
import sys

class DynamicArray():
    
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            raise IndexError("Index out of range")
        return self.A[k]
        
    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = ele
        self.n += 1
    
    def _resize(self, cap):
        B = self.make_array(cap)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = cap
    
    def make_array(self, cap):
        return (cap * ctypes.py_object)()
    

l = DynamicArray()
print(len(l))
l.append(1)
l.append(2)
l.append(3)
print(len(l))
print(l[0], l[1], l[2])

for i in range(20):
    print("Size of l - {0:4d}".format(sys.getsizeof(l)))
    l.append(i)