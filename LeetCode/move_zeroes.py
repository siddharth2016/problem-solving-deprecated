class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastnonzero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[lastnonzero], nums[i] = nums[i], nums[lastnonzero]
                lastnonzero += 1
