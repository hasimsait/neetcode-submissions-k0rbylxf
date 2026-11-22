class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        a=[(x[0],-1*x[1]) for x in intervals]
        a.sort()
        r=0
        cend = -1
        for i in a:
            st,end = i[0],-i[1]
            if end<=cend:
                continue
            else:
                r+=1
                cend = end
        return r