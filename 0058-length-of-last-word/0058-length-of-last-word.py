class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = [i for i in s.strip().split()]
        return len(arr[-1])