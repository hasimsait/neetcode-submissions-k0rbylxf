class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        a=[i for i in range(1,n+1)]
        res = []
        def c(s,l):
            if len(l)==k:
                res.append(l.copy())
                return
            for i in range(s+1,n):
                l.append(a[i])
                c(i,l)
                l.pop()
        c(-1,[])
        return res
