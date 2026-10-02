class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #find most common occuring then greedily spend k is not correct since
        #0,1,2,3,4,5,6,7,100000000,100000000 k=7+6+5+4+3+2+1 -> 8 not 2.
        #you cant decrease values and its the key
        nums.sort()
        l,t=0,0
        for r in range(len(nums)):
            t+=nums[r]
            if (r-l+1)*nums[r]>t+k:
                t-=nums[l]
                l+=1
        return len(nums)-l