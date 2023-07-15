class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'}':'{', ')':'(', ']':'['}

        for c in s:
            if c not in dic:
                stack.append(c)
            else:
                if stack and dic[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return not stack

