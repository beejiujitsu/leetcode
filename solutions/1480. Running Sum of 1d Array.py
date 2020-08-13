class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        def inner(sums: List[int], left: List[int]) -> List[int]:
            if not left:
                return sums
​
            if sums:
                return inner(sums + [sums[-1] + left[0]], left[1:])
​
            return inner([left[0]], left[1:])
        
        return inner([], nums)
