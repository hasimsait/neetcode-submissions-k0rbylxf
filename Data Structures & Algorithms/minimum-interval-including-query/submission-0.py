class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1]*len(queries)
        intervals = [(x[0],x[1],i) for i,x in enumerate(intervals)]
        intervals.sort()
        queries = [(x,i) for i,x in enumerate(queries)]
        queries.sort()
        cranges = []
        t=0
        for q in queries:
            while t<len(intervals) and intervals[t][0]<=q[0]:
                it = intervals[t]
                heapq.heappush(cranges,(it[1]-it[0],it[1]))
                t+=1
            while len(cranges)>0:
                p = heapq.heappop(cranges)
                if p[1]>=q[0]:
                    heapq.heappush(cranges,p)
                    res[q[1]] = p[0]+1
                    break
        return res