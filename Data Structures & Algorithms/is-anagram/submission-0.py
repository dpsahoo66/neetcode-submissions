class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countOccrS = {}
        countOccrT = {}
        for i in s:
            if i in countOccrS:
                countOccrS[i]+=1
            else:
                countOccrS[i]=1
        for j in t:
            if j in countOccrT:
                countOccrT[j]+=1
            else:
                countOccrT[j]=1
        if countOccrS!=countOccrT:
            return False
        return True
        