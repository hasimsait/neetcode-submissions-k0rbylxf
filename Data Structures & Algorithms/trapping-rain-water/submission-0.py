class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        w,level = 0,0
        while l<r:
            com = min(height[l],height[r])
            if com>level:
                for i in range(l,r):
                    if height[i]<com:
                        w+=com-max(height[i],level)
                level = com
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return w