class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s=sum(nums)
        x=[0]*(len(nums)+1)
        mi,ma=0,nums[0]
        for i in range(len(nums)):
            x[i+1]=x[i]+nums[i]
        for i in range(len(x)-1):
            for j in range(i+1,len(x)):
                if not (j==len(x)-1 and i==0):
                    mi=min(mi,x[j]-x[i])
                ma=max(ma,x[j]-x[i])
        return max(s-mi,ma)

