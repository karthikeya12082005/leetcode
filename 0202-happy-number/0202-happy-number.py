class Solution:
    def isHappy(self, n: int) -> bool:
        def squares(n):
            n = str(n)
            return sum([int(i)**2 for i in n])
        while n > 9:
            n = squares(n)
        return n == 1 or n == 7