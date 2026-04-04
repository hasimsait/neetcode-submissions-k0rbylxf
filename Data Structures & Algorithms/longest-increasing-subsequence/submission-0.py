class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1 for i in nums]
        def s(i):
            if memo[i]!=-1:
                return memo[i]
            l=1
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    l=max(l,1+s(j))
            memo[i]=l
            return l
        z=[s(i) for i in range(len(nums))]
        return max(z)