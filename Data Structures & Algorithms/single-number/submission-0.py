class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i=nums[0]
        for a,b in enumerate(nums):
            if a!=0:
                i=i^b
        return i