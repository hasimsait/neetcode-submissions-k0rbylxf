class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten=[]
        goodc=0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        for x,row in enumerate(grid):
            for y,cell in enumerate(row):
                if cell==2:
                    rotten.append([x,y])
                elif cell==1:
                    goodc+=1
        t=0
        while goodc>0:
            c=0
            rt=[]
            for rot in rotten:
                print(rot,goodc)
                for d in directions:
                    xd = rot[0]+d[0]
                    yd = rot[1]+d[1]
                    if xd>=0 and yd>=0 and xd<len(grid) and yd<len(grid[0]) and grid[xd][yd]==1:
                        c+=1
                        goodc-=1
                        grid[xd][yd]=2
                        rt.append([xd,yd])
            rotten+=rt
            if c==0:
                return -1
            t+=1
        return t