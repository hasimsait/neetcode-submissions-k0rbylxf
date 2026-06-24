class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.t=0
        def s(i,c):
            if i==len(nums):
                if c==target:
                    self.t+=1
                return
            s(i+1,c+nums[i])
            s(i+1,c-nums[i])
        s(0,0)
        return self.t