class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def ina(r,l):
            va=False
            for i in r:
                if len(i)==len(l):
                    f=True
                    for j,v in enumerate(i):
                        f= f and l[j]==v
                    va=va or f
            return va
        def c(s,l,k):
            if len(l)==k and not ina(res,l):
                res.append(l.copy())
                return
            for i in range(s+1,len(nums)):
                l.append(nums[i])
                c(i,l,k)
                l.pop()
        nums.sort()
        for i in range(0,len(nums)+1):
            c(-1,[],i)
        return res
