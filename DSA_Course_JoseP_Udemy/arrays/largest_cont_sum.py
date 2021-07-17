def large_cont_sum(arr):
    
    if len(arr) == 0:
        return 0
    
    max_sum = curr_sum = arr[0]
    
    for val in arr[1:]:
        
        curr_sum = max(curr_sum+val, val)
        
        max_sum = max(curr_sum, max_sum)
    
    return max_sum

print(large_cont_sum([-1, 1, 2, -1, 3, 4, 10, 10, -1, -10]))