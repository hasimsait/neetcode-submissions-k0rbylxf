class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        mem = {}
        def s(i,arrl):
            if (i,arrl) in mem:
                return mem[(i,arrl)]
            if i>=arrl:
                return 0
            b=s(i+1,arrl)
            c=s(i+2,arrl)+nums[i]
            mem[(i,arrl)] = max(b,c)
            return mem[(i,arrl)]
        #if you start from 0, the last house is unavailable
        #if you skip 0, its the same as if you started from 1
        #   which has last house available
        return max(s(0,len(nums)-1),s(1,len(nums)))