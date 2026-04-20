class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        gm=0
        for n in nums:
            if n==1:
                i+=1
                gm=max(gm,i)
            else:
                i=0
        return max(gm,i)