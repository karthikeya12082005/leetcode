class Solution:
    def isValid(self, s: str) -> bool: 
        stack = []
        dict = {")":"(","]":"[","}":"{"}
        for i in s :
            if i in "([{" :
                stack.append(i)
            elif stack and dict[i] == stack[-1]  :
                stack.pop()
            else :
                stack.append(i)
        if stack :
            return False
        else :
            return True