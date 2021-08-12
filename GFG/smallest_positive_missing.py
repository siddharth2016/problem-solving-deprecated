class Solution1:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        j = 0
        for i in range(n):
            if arr[i] <= 0:
                arr[i], arr[j] = arr[j], arr[i]
                j+=1
        brr = arr[j:]
        size = len(brr)
        
        for i in range(size):
            
            if abs(brr[i]) - 1 < size and brr[abs(brr[i]) - 1] > 0:
                brr[abs(brr[i]) - 1] = -brr[abs(brr[i]) - 1]
        
        for i in range(size):
            
            if brr[i] > 0:
                return i+1
        return size + 1
    


##################################################################################

class Solution2:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        brr = []
        for val in arr:
            if val >= 0:
                brr.append(val)
        brr = list(set(brr))
        brr.sort()
        N = len(brr)
        if brr[0]==0:
            for i in range(1, N):
                if brr[i]!=i:
                    return i
            return N
        else:
            for i in range(N):
                if brr[i]!=i+1:
                    return i+1
            return N+1