class Solution:
    def findGCD(self, nums: List[int]) -> int:
        b = max(nums)
        a = min(nums)
        while b != 0:
            a, b = b, a % b
        return a