class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0,c1,c2=0,0,0
        for i in nums:
            if i==0:
                c0+=1
            elif i==1:
                c1+=1
            else: c2+=1
        j=0
        while j<len(nums):
            if j<c0:
                nums[j]=0
            elif j<c0+c1:
                nums[j]=1
            else:
                nums[j]=2
            j+=1

        