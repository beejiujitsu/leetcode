class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) > 2:
            nums.remove(max(nums))
            nums.remove(max(nums))
        return max(nums)
