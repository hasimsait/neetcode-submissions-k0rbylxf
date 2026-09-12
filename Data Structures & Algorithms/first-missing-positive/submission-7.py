class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            if n<0:
                nums[i]=0
        for i,n in enumerate(nums):
            v=abs(n)
            if v<=len(nums) and v>0:
                if nums[v-1]>0:
                    nums[v-1]*=-1
                elif nums[v-1]==0:
                    nums[v-1]=-100003
        print(nums)
        for i in range(len(nums)):
            if nums[i]>=0:
                return i+1
        return len(nums)+1
