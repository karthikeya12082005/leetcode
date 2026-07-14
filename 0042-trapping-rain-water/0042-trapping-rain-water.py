class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        ans = 0
        rm = 0
        lm = 0
        while i < j :
            if height[i] <= height[j] :
                if height[i] < lm :
                    ans += lm - height[i]
                else:
                    lm = height[i]
                i += 1
            elif height[j] < height[i] :
                if height[j] < rm :
                    ans += rm - height[j]
                else :
                    rm = height[j]
                j -= 1
        return ans