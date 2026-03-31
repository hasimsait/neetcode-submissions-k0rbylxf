class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def c(s,l,k):
            if len(l)==k and l not in res:
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
