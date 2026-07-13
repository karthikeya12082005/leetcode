class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        n = len(grid[0])
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if dp[j] + 1 > dp[i]:
                    if all(abs(r[i] - r[j]) <= limit for r in grid):
                        dp[i] = dp[j] + 1
        return max(dp)