class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        nums[:]=[0]+nums
        for i in range(len(nums)):
            for j in range(i+2,len(nums)):
                if (nums[j]-nums[i])%k==0:
                    return True
        return False
