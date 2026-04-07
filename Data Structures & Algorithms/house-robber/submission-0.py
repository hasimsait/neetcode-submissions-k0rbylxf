class Solution:
    def rob(self, nums: List[int]) -> int:
        # 3 9 8 1 7 1 1 ->17 19 greedy wouldnt work
        memo = {}
        def d(i,nums):
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i]+d(i+2,nums),d(i+1,nums))
            return memo[i]
        return d(0,nums)