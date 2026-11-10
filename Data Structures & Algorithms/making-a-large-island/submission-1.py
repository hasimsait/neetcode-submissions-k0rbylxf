class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        from collections import deque
        ct=2
        sizes = defaultdict(int)
        r=0
        def sink(sign,i,j):
            s=deque()
            s.append((i,j))
            while s:
                i,j = s.popleft()
                if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]) and grid[i][j]==1:
                    grid[i][j]=sign
                    sizes[sign]+=1
                    s.append((i+1,j))
                    s.append((i-1,j))
                    s.append((i,j+1))
                    s.append((i,j-1))
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                if cell==1:
                    sink(ct,i,j)
                    ct+=1
        sizes[0]=0
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                if cell==0:
                    neigh=set()
                    if i>0:
                        neigh.add(grid[i-1][j])
                    if j>0:
                        neigh.add(grid[i][j-1])
                    if i<len(grid)-1:
                        neigh.add(grid[i+1][j])
                    if j<len(grid[0])-1:
                        neigh.add(grid[i][j+1])
                    s=1
                    for n in neigh:
                        s+=sizes[n]
                    r=max(r,s)
        for i in sizes:
            r=max(r,sizes[i])
        return r