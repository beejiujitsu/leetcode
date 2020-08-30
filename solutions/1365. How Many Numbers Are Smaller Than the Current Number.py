class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        left = collections.deque(nums)
        total = collections.deque()
        while left:
            num = left.pop()
            total.append(len([n for n in nums[::-1] if n < num]))
        total.reverse()
        return total
