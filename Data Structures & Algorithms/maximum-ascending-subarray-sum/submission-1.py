class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        self.smax = nums[0]
        mem={}
        def incfrom(i,prev):
            if (i,prev) in mem:
                return mem[(i,prev)]
            if i>=len(nums):
                return 0
            fromi = incfrom(i+1,nums[i])
            self.smax = max(self.smax,nums[i]+fromi)
            mem[(i,prev)] =fromi+nums[i]
            if nums[i]<=prev:
                return 0
            return nums[i]+fromi
        incfrom(0,-100)
        return self.smax