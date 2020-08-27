class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = collections.Counter()
        for n in nums:
            d[n] += 1
        for n, c in d.items():
            if c == 1:
                return n
