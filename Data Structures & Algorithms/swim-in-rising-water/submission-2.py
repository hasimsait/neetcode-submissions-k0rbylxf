class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        di = [(1,0),(0,1),(-1,0),(0,-1)]
        mem = {}
        mem[(len(grid)-1,len(grid[0])-1)]=len(grid)**2
        def b(t,i,j):
            print(t,i,j)
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return False
            if grid[i][j]>t:
                t=grid[i][j]
            if (i,j) not in mem or mem[(i,j)]>t:
                for d in di:
                    inew = d[0]+i
                    jnew = d[1]+j
                    heapq.heappush(s,(t,inew,jnew))
                mem[(i,j)] = t
                return True
            if (i,j) in mem:
                return True
            return False
        s=[]
        heapq.heappush(s,(max(0,grid[0][0]),0,0))
        imp = True
        while s and mem[(len(grid)-1,len(grid[0])-1)]==len(grid)**2:
            t,i,j=heapq.heappop(s)
            b(t,i,j)
        return mem[(len(grid)-1,len(grid[0])-1)]