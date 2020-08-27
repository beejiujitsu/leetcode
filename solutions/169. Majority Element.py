class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = collections.Counter()
        for n in nums:
            d[n] += 1
        for i, v in d.items():
            if v == max(d.values()):
                return i
