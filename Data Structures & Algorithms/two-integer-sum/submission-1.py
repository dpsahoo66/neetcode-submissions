class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff not in hmap:
                hmap[nums[i]] = i
            else:
                return [hmap[diff],i]

        