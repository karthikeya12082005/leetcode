class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        x=sorted(zip(difficulty,profit))
        worker.sort()
        ans=best=i=0
        for j in worker:
            while i<len(x) and x[i][0]<=j:
                best=max(best,x[i][1])
                i+=1
            ans+=best
        return ans