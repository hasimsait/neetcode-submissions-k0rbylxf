class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        self.m = 0
        def s(i,dire,prev):
            if i>=len(nums):
                return 0
            if (nums[i]>prev and dire>0) or (nums[i]<prev and dire<0):
                a = 1+s(i+1,dire,nums[i])
                self.m = max(self.m, a)
                return a
            else:
                a=s(i+1,dire,nums[i])
                return 0
        s(1,1,nums[0])
        s(1,-1,nums[0])
        return self.m +1
            
