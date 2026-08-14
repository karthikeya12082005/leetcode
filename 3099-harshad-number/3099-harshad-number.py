class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        a=str(x)
        ans=0
        for i in a:
            ans+=int(i)
        if x%ans==0:
            return ans
        else:
            return -1
        