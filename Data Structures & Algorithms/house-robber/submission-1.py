class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def d(i,nums):
            if i>=len(nums):
                return 0
            if i not in memo:
                memo[i] = max(nums[i]+d(i+2,nums),d(i+1,nums))
            return memo[i]
        return d(0,nums)