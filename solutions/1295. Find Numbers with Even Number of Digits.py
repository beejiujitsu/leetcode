class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([n for n in nums if not len(str(n)) % 2])
