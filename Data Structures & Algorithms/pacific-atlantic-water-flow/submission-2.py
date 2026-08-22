class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights[0]),len(heights)
        pac = [[False] * m for _ in range(n)]
        atl = [[False] * m for _ in range(n)]
        def dfs(i, j, ocean):
            ocean[i][j] = True
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and not ocean[ni][nj]:
                    if heights[ni][nj] >= heights[i][j]:
                        dfs(ni, nj, ocean)    
        for i in range(n):
            dfs(i, 0, pac)
            dfs(i, m - 1, atl)

        for j in range(m):
            dfs(0, j, pac)
            dfs(n - 1, j, atl)

        return [[i, j] for i in range(n) for j in range(m) if pac[i][j] and atl[i][j]]