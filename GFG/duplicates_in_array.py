class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	arr_size = n
        for i in range(arr_size):
            x = arr[i] % arr_size
            arr[x] = arr[x] + arr_size
        res = []
        for i in range(arr_size):
            if (arr[i] >= arr_size*2):
                res.append(i)
        return [-1] if len(res) == 0 else res