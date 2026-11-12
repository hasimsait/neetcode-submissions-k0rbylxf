class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        c=defaultdict(int)
        l=m=0
        for i,n in enumerate(nums):
            c[n]+=1
            while c[n]>k:
                c[nums[l]]-=1
                l+=1
            m=max(i-l+1,m)
        return m
