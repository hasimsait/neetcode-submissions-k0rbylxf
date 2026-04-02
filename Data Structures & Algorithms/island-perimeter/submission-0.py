class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dire = [[0,1],[0,-1],[1,0],[-1,0]]
        def sink(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
                return 1
            if grid[i][j]==-1:
                return 0
            grid[i][j]=-1
            a=0
            for d in dire:
                b=sink(i+d[0],j+d[1])
                a+=b
            return a
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return sink(i,j)

