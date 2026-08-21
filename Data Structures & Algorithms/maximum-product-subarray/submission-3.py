class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n,maxP,c = len(nums),nums[0],0
        for i in range(n):
            c=nums[i]*(c or 1)
            maxP=max(maxP,c)
        c=0
        for i in range(n):
            c=nums[-i-1]*(c or 1)
            maxP=max(maxP,c)
        return maxP        