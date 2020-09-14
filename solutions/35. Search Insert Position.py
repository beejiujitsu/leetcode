class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            for i in range(len(nums)):
                if target <= nums[i]:
                    return i
            else:
                return len(nums) 
