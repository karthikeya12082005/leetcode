class Solution:
    def countSpecialIntegers(self, nums: List[int]) -> int:
        pos = {}
        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = []
            pos[x].append(i)
        ans = 0
        for indices in pos.values(): 
            if len(indices) == 3:     
                if indices[0] + indices[2] == 2 * indices[1]:
                    ans += 1
        return ans