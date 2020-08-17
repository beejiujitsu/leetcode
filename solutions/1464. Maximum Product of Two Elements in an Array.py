class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max(nums)
        nums2 = nums.copy()
        i = nums.index(max1)
        nums2.pop(i)
        max2 = max(nums2)
        j = nums.index(max2)
        return (nums[i]-1)*(nums[j]-1)
