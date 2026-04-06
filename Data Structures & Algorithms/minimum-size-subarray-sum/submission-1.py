class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        l,r,s=0,0,0
        minl = 200000
        while r<=len(nums):
            while s<target and r<len(nums):
                s+=nums[r]
                r+=1
            #we have subarray i,j that satisfies target or is out of bounds
            while s>=target and l<=r:
                minl = min(minl,r-l)
                s-=nums[l]
                l+=1
            #we have subarray x,y that no longer satisfies target
            if r<len(nums):
                s+=nums[r]
            r+=1
        return minl