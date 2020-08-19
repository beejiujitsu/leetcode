class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def inner():
            i = 0
            while i + 1 < len(nums):
                prev = nums[i - 1]
                cur = nums[i]
                nxt = nums[i + 1]
                if cur > prev and cur > nxt:
                    return i
                i += 1
            return i
        return inner() 
