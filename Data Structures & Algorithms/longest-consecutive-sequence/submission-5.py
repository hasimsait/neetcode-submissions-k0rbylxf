class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<=1:
            return len(nums)
        l,r,p,m,cl=0,0,None,0,0
        while r<len(nums):
            if p is not None and nums[r] in [p,p+1]:
                if nums[r]==p+1:
                    cl+=1
                p=nums[r]
            else:
                l=r
                cl=1
                p=nums[r]
            m=max(m,cl)
            r+=1
        return m


