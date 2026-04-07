class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        stack = [[0,0,0]]
        vis = [[0 for i in row] for row in heights]
        d=[[0,1],[0,-1],[1,0],[-1,0]]
        m,n = len(heights),len(heights[0])
        while stack:
            c,x,y=heapq.heappop(stack)
            if x==m-1 and y==n-1:
                return c
            if vis[x][y]==1:
                #it wasn't visited at time of insertion but some cheaper path visited it
                continue
            vis[x][y]=1
            for i in d:
                ix = x+i[0]
                iy = y+i[1]
                if ix>=0 and iy>=0 and ix<m and iy<n and vis[ix][iy]==0:
                    e= abs(heights[x][y]-heights[ix][iy])
                    heapq.heappush(stack,[max(e,c),ix,iy])
        return 0

            

