class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        total = sum(nums)

        if total <= k:
            return 0

        n = (total - 1)//k

        return (n*(n + 1)//2)%MOD