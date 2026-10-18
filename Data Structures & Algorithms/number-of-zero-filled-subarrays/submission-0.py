class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l,r,a=-1,0,0
        nums.append(1)
        while r<len(nums):
            if nums[r]==0:
                if l==-1:
                    l=r
            elif l!=-1:
                #end of a 0 section:
                a+=(r-l+1)*(r-l)//2
                l=-1
            r+=1
        return a