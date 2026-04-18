class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        appearsInTrusts = set()
        trusted = {}
        for t in trust:
            appearsInTrusts.add(t[0])
            if t[1] not in trusted:
                trusted[t[1]] = []
            trusted[t[1]].append(t[0])
        for i in range(1,n+1):
            if i in trusted and len(trusted[i])==n-1 and i not in appearsInTrusts:
                return i
        return -1