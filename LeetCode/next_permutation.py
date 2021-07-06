class Solution:
    def reverse(self, nums: List[int], i: int) -> None:
        end = len(nums) - 1
        while i < end:
            nums[i], nums[end] = nums[end], nums[i]
            i, end = i+1, end-1
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = len(nums) - 2
        while last>=0 and nums[last+1]<=nums[last]:
            last-=1
        if last>=0:
            last2 = len(nums) - 1
            while(nums[last2] <= nums[last]):
                last2 -= 1
            nums[last2], nums[last] = nums[last], nums[last2]
        self.reverse(nums, last+1)
