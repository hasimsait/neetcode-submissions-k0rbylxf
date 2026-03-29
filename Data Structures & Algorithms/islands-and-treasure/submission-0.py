class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        stack=[]
        for x,row in enumerate(grid):
            for y,cell in enumerate(row):
                if cell==0:
                    stack.append([x,y,0])
        dire=[[0,-1],[-1,0],[1,0],[0,1]]
        while len(stack)>0:
            a=stack[0]
            ax,ay,av=a[0],a[1],a[2]
            stack=stack[1:]
            if ax<0 or ax>=len(grid) or ay<0 or ay>=len(grid[0]) or grid[ax][ay] ==-1:
                continue
            elif grid[ax][ay]>0 and grid[ax][ay]<2147483647:
                continue
            else:
                grid[ax][ay]=min(grid[ax][ay],av)
                for d in dire:
                    stack.append([ax+d[0],ay+d[1],av+1])
        print(grid)
