"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        inte=[[x.start,x.end] for x in intervals]
        inte.sort()
        ends = []
        for i in inte:
            j=0
            while j<len(ends):
                if ends[j]<=i[0]:
                    break
                j+=1
            if j!=len(ends):
                ends[j]=i[1]
            else:
                ends.append(i[1])
        return len(ends)