class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = nums + [0]
        m = 0
        n = 0 
        for i in nums:
            if i:
                n = n + 1
            else:
                if n > m:
                    m = n
                n = 0
        return m