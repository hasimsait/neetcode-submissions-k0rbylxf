class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        c=nums[0]%2
        for i in range(1,len(nums)):
            if nums[i]%2 == c:
                return False
            c=nums[i]%2
        return True