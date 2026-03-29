class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.directions=[[0,1],[1,0],[0,-1],[-1,0]]
        def sink(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
                return 0
            grid[i][j]=0
            a=1
            for direction in self.directions:
                a+=sink(i+direction[0],j+direction[1])
            return a
        maxx=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxx=max(maxx,sink(i,j))
        return maxx
            