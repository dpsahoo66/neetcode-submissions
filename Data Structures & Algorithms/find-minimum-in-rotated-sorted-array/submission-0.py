class Solution:
    def findMin(self, nums: List[int]) -> int:
        maxElement = max(nums)
        i = nums.index(maxElement)
        if i==len(nums)-1:
            return nums[0]
        else:
            return nums[i+1]
        