class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        nums.sort()
        if s==0 or s%2==1:
            return False
        t=s//2
        mem = {}
        def p(i,cs):
            if cs == t:
                return True
            if i>=len(nums) or cs+nums[i]>t:
                return False
            if (i,cs) not in mem:
                mem[(i,cs)]= p(i+1,cs+nums[i]) or p(i+1,cs)
            return mem[(i,cs)]
        return p(0,0)

    