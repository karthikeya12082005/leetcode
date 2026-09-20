class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1 or s == s[::-1]:
            return s
        start, max_len = 0, 1
        i = 0
        while i < n:
            if (n - i) <= max_len // 2:
                break
            l = r = i
            while r < n - 1 and s[r] == s[r + 1]:
                r += 1
            i = r + 1
            while r < n - 1 and l > 0 and s[r + 1] == s[l - 1]:
                r += 1
                l -= 1
            length = r - l + 1
            if length > max_len:
                start = l
                max_len = length

        return s[start:start + max_len]