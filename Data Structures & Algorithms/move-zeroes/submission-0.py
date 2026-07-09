class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ct=0
        pt=0
        while pt<len(nums):
            if nums[pt]==0:
                nums[:] = nums[:pt] + nums[pt+1:]
                ct+=1
            else:
                pt+=1
        nums[:]= nums + [0]*ct