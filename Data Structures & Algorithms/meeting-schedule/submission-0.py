"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0:
            return True
        c=[]
        for i in intervals:
            c.append([i.start,i.end])
        c.sort()
        cend=c[0][0]
        for i in c:
            if i[0]>=cend:
                cend = i[1]
            else:return False
        return True