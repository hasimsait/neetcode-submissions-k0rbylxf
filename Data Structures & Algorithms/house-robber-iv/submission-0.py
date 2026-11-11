class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l,r = min(nums),max(nums)
        n=r
        while l<=r:
            m=(l+r)//2
            ct,i=0,0
            while i<len(nums):
                if nums[i]<=m:
                    ct+=1
                    i+=2
                else:
                    i+=1
            if ct>=k:
                r=m-1
                n=m
            else:
                l=m+1
        return n

