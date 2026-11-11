class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        blocked = {(x[0],x[1]) for x in walls}
        for g in guards:
            blocked.add((g[0],g[1]))
        sunk =set()
        def sink(i,j):
            ti,tj = i,j
            for di,dj in  [(1,0),(0,1),(-1,0),(0,-1)]:
                i,j = ti+di,tj+dj
                while i<m and j<n and i>=0 and j>=0 and (i,j) not in blocked:
                    sunk.add((i,j))
                    i+=di
                    j+=dj
        for gi,gj in guards:
            sink(gi,gj)
        return m*n-len(sunk|blocked)

                
