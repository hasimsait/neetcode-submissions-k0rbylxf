class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        def bs(v):
            l,r=0,n-1
            while l<=r:
                m=(l+r)//2
                if nums[m]>=v:
                    r=m-1
                else:
                    l=m+1
            return l
        s=bs(target)
        if s==n or nums[s]!=target:
            return [-1,-1]
        return [s,bs(target+1)-1]