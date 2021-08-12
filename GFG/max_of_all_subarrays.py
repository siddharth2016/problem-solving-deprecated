from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        dq = deque()
        res = []
        
        for i in range(k):
            
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()

            dq.append(i)
        
        for i in range(k, n):
            
            res.append(arr[dq[0]])
            
            while dq and dq[0] <= i-k:
                dq.popleft()
                
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
                
            dq.append(i)
            
        res.append(arr[dq[0]])
        
        return res