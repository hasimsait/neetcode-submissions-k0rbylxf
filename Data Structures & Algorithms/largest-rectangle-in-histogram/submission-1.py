class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #were not leaving money on the table its the height of one of the bars
        #left to right pop while larger than cur then ins
        #right to left do same
        #max area =max for each i as far as they can extend to r and l * heights[i]
        n=len(heights)
        s=[]
        l=[-1]*n
        for i in range(n):
            while s and heights[s[-1]]>=heights[i]:
                s.pop()
            if s:
                l[i]=s[-1]
            s.append(i)
        s=[]
        r=[n]*n
        for i in range(n)[::-1]:
            while s and heights[s[-1]]>=heights[i]:
                s.pop()
            if s:
                r[i]=s[-1]
            s.append(i)
        m=0
        for i in range(n):
            l[i]+=1
            r[i]-=1
            m=max(m,heights[i]*(r[i]-l[i]+1))
        return m