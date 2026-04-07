class Solution:
    def jump(self, nums: List[int]) -> int:
        nums[-1]=0
        #from right to left excluding last
        for s in [i for i in range(len(nums)-1)][::-1]:
            #number of steps you need to take from this step to end = minimum within your reach +1
            nums[s]=len(nums) if nums[s]==0 else min(nums[s+1:s+nums[s]+1])+1
        return nums[0]