class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c,r=0,0
        while r<len(nums):
            if nums[c-1]!=nums[r]:
                nums[c]=nums[r]
                c+=1
                if r+1<len(nums) and nums[r+1]==nums[r]:
                    nums[c]=nums[r]
                    c+=1
            r+=1
        return c