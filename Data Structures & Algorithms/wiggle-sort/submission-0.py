class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            if (nums[i]<nums[i-1] and i%2==1) or (nums[i]>nums[i-1] and i%2==0):
                nums[i],nums[i-1]=nums[i-1],nums[i]