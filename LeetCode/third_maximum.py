class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        minimum = min(nums)
        first, second, third = minimum, minimum, minimum
        spaned = {}
        for n in nums:
            if n in spaned:
                continue
            if first<n:
                third, second, first = second, first, n
            elif second<n:
                third, second = second, n
            elif third<n:
                third = n
            spaned[n] = 1
        return third if third!=second else first
