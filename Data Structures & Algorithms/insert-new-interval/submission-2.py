class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return[newInterval]
        if intervals[0][0]>newInterval[1]:
            return [newInterval]+intervals
        if intervals[-1][1]<newInterval[0]:
            return intervals+[newInterval]
        i=[]
        j=0
        while j<len(intervals):
            if intervals[j][1]<newInterval[0]:
                i.append(intervals[j])
            else:
                break
            j+=1
        #intervals[j] is the first intersecting interval
        start = min(intervals[j][0],newInterval[0])
        while j<len(intervals):
            if intervals[j][0]<=newInterval[1]:
                j+=1
            else:
                break
        end = max(intervals[j-1][1],newInterval[1])
        i.append([start,end])
        #j now is the first non intersecting interval
        i+=intervals[j:]
        return i
