class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c=0
        must=0
        for i in range(len(nums)):
            c+=nums[i]
            must+=i
        must+=len(nums)
        return must-c