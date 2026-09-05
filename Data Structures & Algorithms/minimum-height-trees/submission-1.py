class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import deque
        if n==1:
            return[0]
        fromto = defaultdict(set)
        for edge in edges:
            fromto[edge[0]].add(edge[1])
            fromto[edge[1]].add(edge[0])
        r={}
        for n in fromto:
            s=deque([(n,0)])
            vis =set()
            while len(vis)<len(fromto) and s:
                a,c =s.popleft()
                if a in vis:
                    continue
                vis.add(a)
                for node in fromto[a]:
                    s.append((node,c+1))
            r[n]=c
        minh = float("inf")
        for n in r:
            minh=min(r[n],minh)
        c=[]
        for n in r:
            if r[n]==minh:
                c.append(n)
        return c