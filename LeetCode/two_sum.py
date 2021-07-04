class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        a,b = -1,-1
        for i,n in enumerate(nums):
            diff = target - n
            if diff in indexes:
                a = i
                b = indexes[diff]
                break
            indexes[n] = i
        return [a, b]
        
