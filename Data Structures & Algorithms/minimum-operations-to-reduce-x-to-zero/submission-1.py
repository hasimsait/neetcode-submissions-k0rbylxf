class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s=sum(nums)
        if s<x:
            return -1
        l,r,cs,t = 0,0,0,s-x
        m=-1
        while l<len(nums) and r<=len(nums):
            if cs<t:
                if r<len(nums):
                    cs+=nums[r]
                r+=1
            elif cs==t:
                m=max(m,r-l)
                cs-=nums[l]
                l+=1
            else:
                cs-=nums[l]
                l+=1
        return len(nums)-m if m>=0 else -1


