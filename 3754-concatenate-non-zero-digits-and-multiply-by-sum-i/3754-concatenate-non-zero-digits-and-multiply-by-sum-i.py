class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        s = str(n)
        x = '0'
        add = 0
        for i in s:
            if i == '0':
                continue
            x += i
            add += int(i)
        return int(x) * add        
        