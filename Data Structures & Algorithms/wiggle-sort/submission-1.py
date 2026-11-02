class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        l,r=1,len(nums)-1
        if not len(nums)%2:
            r-=1
        large = True
        while l<r:
            if large:
                nums[l],nums[r]=nums[r],nums[l]
            large=not large
            l+=1
            r-=1