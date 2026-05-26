class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        direction = 0
        prev = nums[0]
        for i in range(1,len(nums)):
            if direction==0:
                if nums[i]>prev:
                    direction = 1
                elif nums[i]<prev:
                    direction = -1
            elif direction==1:
                if nums[i]<prev:
                    return False
            elif direction==-1:
                if nums[i]>prev:
                    return False
            prev = nums[i]
        return True
