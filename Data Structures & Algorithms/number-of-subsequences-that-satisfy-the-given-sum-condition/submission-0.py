class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        M=10**9+7
        res=0
        nums.sort()
        l,r = 0,len(nums)-1
        while l<=r:
            if nums[l]+nums[r]<=target:
                res= (res+2**(r-l))%M
                l+=1
            else:
                r-=1
        return res