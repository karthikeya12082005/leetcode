class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX_XOR = 2048
        present = [False] * MAX_XOR
        for a in nums:
            for b in nums:
                present[a^b] = True
        ans = [False] * MAX_XOR
        for x in range(MAX_XOR):
            if present[x]:
                for a in nums:
                    ans[x^a] = True
        return sum(ans)