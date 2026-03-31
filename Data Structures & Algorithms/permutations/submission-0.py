class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def c(l,k):
            if len(l)==k:
                res.append(l.copy())
                return
            for i in range(len(nums)):
                if i not in l:
                    l.append(i)
                    c(l,k)
                    l.pop()
        c([],len(nums))
        for i,l in enumerate(res):
            res[i]=[nums[x] for x in l]

        return res