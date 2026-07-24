class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        arr[:] = arr[::-1]
        st = ""
        for i in arr:
            st += " "
            st += i 
        return st[1:]