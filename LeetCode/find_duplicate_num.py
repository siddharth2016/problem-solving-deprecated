class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t = h = nums[0]
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if t == h:
                break
        t = nums[0]
        while t!=h:
            t = nums[t]
            h = nums[h]
        return h
