class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        from itertools import accumulate
        return accumulate(nums)
