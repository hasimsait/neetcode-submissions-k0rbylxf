class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if len(nums)==1:
            if nums[0]==0:
                return 0
            return 1 if nums[0]>0 else -1
        return self.arraySign(nums[:len(nums)//2])*self.arraySign(nums[len(nums)//2:])
        