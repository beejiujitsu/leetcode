class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        for i, v in enumerate(nums):
            if i == 0:
                continue
            if nums[i - 1] != v - 1:
                return v - 1
            if i == len(nums) - 1:
                return v + 1
        else:
            return nums[0] + 1
