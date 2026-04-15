class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges=[]
        for i,x in enumerate(points):
            for offset in range(1,len(points)-i):
                xx,xy,yx,yy=x[0],x[1],points[i+offset][0],points[i+offset][1]
                edges.append([abs(xx-yx)+abs(xy-yy),i,offset+i])
        edges.sort(reverse=True)
        pts = [set() for x in range(len(points))]
        adp = [i for i in range(len(points))]
        for p in range(len(points)):
            pts[p].add(p)
        cost=0
        maxc=1
        while maxc<len(points):#while the graph is not connected
            if len(edges)<=0:
                return -1
            cheapestEdge = edges.pop()
            c,x,y=cheapestEdge
            ax,ay=adp[x],adp[y]
            if ax==ay:
                continue
            else:
                cost+=c
                for e in pts[ay]:
                    pts[ax].add(e)
                    adp[e]=ax
                maxc=max(maxc,len(pts[ax]))
                pts[ay]=set()
        return cost

        

        
    
        