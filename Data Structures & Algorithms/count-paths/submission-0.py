class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}
        def d(i,j):
            if (i,j) in mem:
                return mem[(i,j)]
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            a=d(i+1,j)
            b=d(i,j+1)
            mem[(i,j)] = a+b
            return a+b
        return d(0,0)