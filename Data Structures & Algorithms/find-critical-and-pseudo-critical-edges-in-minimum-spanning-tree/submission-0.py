class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i,edge in enumerate(edges):
            edge.append(i)
        con = defaultdict(list)
        for src,dst,w,idx in edges:
            con[src].append((dst,w,idx))
            con[dst].append((src,w,idx))
        def m(src,dst,exc):
        #shortest path from src to dst without edge exc.
            d=[float('inf')]*n
            d[src]=0
            q=[(0,src)]
            while q:
                max_w,cn = heapq.heappop(q)
                if cn==dst:
                    return max_w
                for node in con[cn]:
                    if node[2]==exc:
                        continue
                    nw=max(max_w,node[1])
                    if nw<d[node[0]]:
                        #greeeed
                        d[node[0]]=nw
                        heapq.heappush(q,(nw,node[0]))
            return float('inf')


        r1,r2=[],[]
        for k,(i,j,w,idx) in enumerate(edges):
            if w<m(i,j,idx):
                r1.append(idx)
            elif w==m(i,j,-1):
                r2.append(idx)
        return [r1,r2]