class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges=[]
        for i,x in enumerate(points):
            for offset in range(1,len(points)-i):
                xx,xy,yx,yy=x[0],x[1],points[i+offset][0],points[i+offset][1]
                edges.append([abs(xx-yx)+abs(xy-yy),i,offset+i])
        edges.sort(reverse=True)
        #djikstra like cost,index1,index2
        pts = [set() for x in range(len(points))]#each pt is connected to itself
        for p in range(len(points)):
            pts[p].add(p)
        adp = [i for i in range(len(points))]
        cost=0
        maxc=1
        while maxc<len(points):#while the graph is not connected
            if len(edges)<=0:
                return -1
            c,x,y = edges.pop()
            ax,ay=adp[x],adp[y]
            if ax==ay:#were not improving the connectivity, skip edge
                continue
            else:
                cost+=c
                for e in pts[ay]:
                    pts[ax].add(e)
                    adp[e]=ax
                maxc=max(maxc,len(pts[ax]))
                #pts[ay]=set() #if you del you'd need to shift adp vals
        return cost

        

        
    
        