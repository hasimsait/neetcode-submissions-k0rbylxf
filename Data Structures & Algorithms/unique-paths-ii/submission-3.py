class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dire = [[0,1],[1,0]]
        mem={}
        def dfs(x,y):
            if (x,y) in mem:
                return mem[(x,y)]
            if x>=len(obstacleGrid) or y>=len(obstacleGrid[0]):
                return 0
            if obstacleGrid[x][y] ==1:
                return 0
            if x==len(obstacleGrid)-1 and y==len(obstacleGrid[0])-1:
                return 1


            s=0
            for d in dire:
                tx=x+d[0]
                ty=y+d[1]
                s+=dfs(tx,ty)
            mem[(x,y)]=s
            return s
        return dfs(0,0)