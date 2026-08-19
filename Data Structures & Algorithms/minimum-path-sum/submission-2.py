class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        from functools import lru_cache
        a=[(0,0,0)]
        m,n=len(grid),len(grid[0])
        @lru_cache(400)
        def s(i,j):
            if i==m-1 and j==n-1:
                return grid[i][j]
            if i<m and j<n:
                return min(s(i+1,j),s(i,j+1))+grid[i][j]
            return 400*201
        return s(0,0)
        
            
            
