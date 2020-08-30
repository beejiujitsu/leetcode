class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        left = collections.deque(nums)
        total = collections.deque()
        while left:
            num = left.popleft()
            total.append(len([n for n in nums if n < num]))
        return total
