class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(len(first)):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans