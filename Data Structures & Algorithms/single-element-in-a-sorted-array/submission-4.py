class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r,n = 0,len(nums)-1,0
        while l<r:
            m=(l+r)//2
            if m^1<len(nums) and nums[m^1]!=nums[m]:
                r=m
            else:
                l=m+1
        return nums[l]