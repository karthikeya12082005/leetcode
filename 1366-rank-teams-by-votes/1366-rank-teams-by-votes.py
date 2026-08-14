class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = dict()
        n = len(votes[0])
        for team in votes[0]:
            d[team] = [0] * n
        for vote in votes:
            for i, team in enumerate(vote):
                d[team][i] += 1
        res = sorted(d.keys())
        res.sort(key=d.get, reverse=True)
        return "".join(res)
            