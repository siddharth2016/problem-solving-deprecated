def maxSubArraySum(array):
	'''
	Returns the maximum subarray sum.
	
	array (list): A list of numbers.
	'''
	# Complete this function
	maxSum = currSum = array[0]
	
	for val in array[1:]:
	    
	    currSum = max(currSum+val, val)
	    
	    maxSum = max(maxSum, currSum)
	   
	return maxSum