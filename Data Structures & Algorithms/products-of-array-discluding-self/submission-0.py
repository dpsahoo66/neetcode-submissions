class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i=0
        res=[]
        while i<len(nums):
            pr = 1
            for j in range(len(nums)):
                if i!=j:
                    pr*=nums[j]
            res.append(pr)
            i+=1
        return res

        