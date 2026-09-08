class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = max(nums)
        points = [0] * (m + 1)
        for x in nums:
            points[x] += x
        dp = [0] * (m + 1)
        for i in range(1, m + 1):
            take = points[i]
            if i >= 2:
                take += dp[i - 2]
            nottake = dp[i - 1]
            dp[i] = max(take, nottake)
        return dp[m]