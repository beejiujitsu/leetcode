class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def inner(total: List[int], left: List[int]) -> List[int]:
            if not left:
                return total
            num = left[0]
            return inner(total + [len([n for n in nums if n < num])], left[1:])
        return inner([], nums)
