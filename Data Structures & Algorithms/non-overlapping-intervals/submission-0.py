class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        r = 0 
        p = intervals[0][1]
        i=1
        while i<len(intervals):
            s,e=intervals[i]
            if s >= p:
                p=e
            else:
                r+=1
                p=min(e,p)
            i+=1
        return r
