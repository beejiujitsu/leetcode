from contextlib import suppress
​
​
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        for n in nums:
            sums.append((sums[-1] + n if sums else n))
        return sums
