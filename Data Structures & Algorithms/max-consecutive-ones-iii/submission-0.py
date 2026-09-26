class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r,kct,ans=0,0,0,0
        while r<len(nums):
            if nums[r]==0:
                kct+=1
            while kct>k:
                if nums[l]==0:
                    kct-=1
                l+=1
            r+=1
            ans = max(ans,r-l)
        return ans
            