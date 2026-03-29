class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lastExists = False
        zeroExists = False
        for i in range(len(nums)):
            if abs(nums[i])==len(nums):
                lastExists = True
            elif abs(nums[i])>len(nums):
                continue
            else:
                if abs(nums[i])==0:
                    zeroExists = True
                c= nums[abs(nums[i])]
                if c==0:
                    zeroExists = True
                    nums[abs(nums[i])]=-2*len(nums)
                else:
                    nums[abs(nums[i])]*=-1
        print(nums,zeroExists,lastExists)
        if lastExists is False:
            return len(nums)
        if zeroExists is False:
            return 0
        for i in range(1,len(nums)):
            if nums[i]>=0:
                return i
        return 0