class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res,l,p = 0,0,1
        for r in range(len(nums)):
            p*=nums[r]
            while l<=r and p>=k:
                p=p//nums[l]
                l+=1
            res+=(r-l+1)
        return res