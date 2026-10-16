class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        t=sum(grid[0])
        b=0
        r=t
        for j in range(len(grid[0])):
            t-=grid[0][j]
            r=min(r,max(t,b))
            b+=grid[1][j]
        return r
