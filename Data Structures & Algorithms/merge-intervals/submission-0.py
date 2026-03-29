class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        currend=intervals[0][1]
        c=[intervals[0]]
        for i in intervals:
            if i[0]>currend:
                c.append(i)
                currend = i[1]
            else:
                c[-1] = [c[-1][0],max(c[-1][1],i[1])]
                currend = c[-1][1]
        return c