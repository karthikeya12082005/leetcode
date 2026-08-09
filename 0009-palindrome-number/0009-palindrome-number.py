class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            y = str(x)
            y = y[::-1]
            y = int(y)
            return x == y
        return False