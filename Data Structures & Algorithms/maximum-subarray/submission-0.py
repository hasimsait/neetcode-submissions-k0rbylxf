class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo={}
        self.gmax = nums[0]
        if len(nums)==0:
            return 0
        def x(i,j):
            if i>j or i<0 or j>len(nums):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if i==(j-1):
                memo[(i,j)]=nums[i]
                self.gmax = max(self.gmax,memo[(i,j)])
            else:
                memo[(i,j)]=max(nums[i],nums[i]+x(i+1,j))
                self.gmax = max(self.gmax,memo[(i,j)])
            return memo[(i,j)]
        x(0,len(nums))
        return self.gmax
                
        