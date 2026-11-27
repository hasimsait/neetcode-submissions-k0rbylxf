class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        a=[row.copy() for row in grid]
        if not grid:
            return grid
        s=len(grid)*len(grid[0])
        x=len(grid[0])
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                a[((i*x+j+k+s)%s)//x][((i*x+j+k+s)%s)%x]=cell
        return a


