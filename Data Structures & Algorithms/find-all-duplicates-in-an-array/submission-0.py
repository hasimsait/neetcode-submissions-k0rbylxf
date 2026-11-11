class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        r=[]
        for n in nums:
            n=abs(n)
            if nums[n-1]<0:
                r.append(n)
            else:
                nums[n-1]*=-1
        return r
