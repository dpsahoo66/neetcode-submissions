class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newStr=''
        for i in s:
            if i.isalnum():
                newStr+=i
        i,j=0,len(newStr)-1
        while i<j:
            if newStr[i]!=newStr[j]:
                return False
            i+=1
            j-=1
        return True
        