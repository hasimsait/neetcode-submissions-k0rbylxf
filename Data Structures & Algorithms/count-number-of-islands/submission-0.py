class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        c=0
        def sink(i,j):
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[i]) and grid[i][j]=="1":
                grid[i][j]="0"
                sink(i-1,j)
                sink(i+1,j)
                sink(i,j-1)
                sink(i,j+1)
        for i,r in enumerate(grid):
            for j,cell in enumerate(r):
                if cell=="1":
                    c+=1
                    sink(i,j)
        return c
                