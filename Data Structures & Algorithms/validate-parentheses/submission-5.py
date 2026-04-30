class Solution:
    def isValid(self, s: str) -> bool:
        check=[]
        for i in s:
            if i in '({[':
                check.append(i)
            elif check and ((check[-1] == '(' and i == ')') or (check[-1] == '[' and i == ']') or (check[-1] == '{' and i == '}')):
                check.pop()
            else:
                return False
        if len(check)==0:
            return True
        else:
            return False