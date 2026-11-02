class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        a=defaultdict(int)
        m=0
        for i,row in enumerate(wall):
            c=0
            for e in row[:len(row)-1]:
                c+=e
                a[c]+=1
                m=max(m,a[c])
        return len(wall)-m
                