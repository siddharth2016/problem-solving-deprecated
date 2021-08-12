class Solution:
    #Function to find the length of longest subarray of even and odd numbers.
    def maxEvenOdd(self,arr,n):
        maxl = 1
        if len(arr)==1:
            return maxl
        
        for i in range(n):
            arr[i] %= 2
        i = 0
        
        for j in range(1, n):
            if arr[j-1] == arr[j]:
                maxl = max(maxl, j-i)
                i = j
            else:
                maxl = max(maxl, j-i+1)
        return maxl