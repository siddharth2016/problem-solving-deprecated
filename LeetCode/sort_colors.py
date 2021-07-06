class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        ones = nums.count(1)+zeros
        twos = nums.count(2)+ones
        cur = 0
        while cur<zeros:
            nums[cur] = 0
            cur+=1
        while cur<ones:
            nums[cur] = 1
            cur+=1
        while cur<twos:
            nums[cur] = 2
            cur+=1
        
