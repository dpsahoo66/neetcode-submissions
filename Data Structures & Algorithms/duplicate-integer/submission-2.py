class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap={}
        flag=1
        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                flag=0
                hmap[i] += 1
                return True
        if flag==1:
            return False
        