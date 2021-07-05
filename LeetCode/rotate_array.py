class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        newList = []
        for i in range(n - k%n, n):
            newList.append(nums[i])
        for i in range(0, n - k%n):
            newList.append(nums[i])
        for i in range(n):
            nums[i] = newList[i]
        
