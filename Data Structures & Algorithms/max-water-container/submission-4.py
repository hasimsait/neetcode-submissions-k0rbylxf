class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j,s=0,len(heights)-1,0
        while i<j:
            s=max(s,min(heights[i],heights[j])*(j-i))
            if heights[j]<heights[i]:
                j-=1
            else:
                i+=1
        return s