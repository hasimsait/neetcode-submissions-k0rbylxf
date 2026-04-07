class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        neigh = {i:[] for i in range(n)}
        for flight in flights:
            neigh[flight[0]].append([flight[1],flight[2]])
        stack = [[0,src,0]]
        visited = {} #due to max steps, we may need to take a suboptimal route.
        if src == dst:
            return 0
        while stack:
            c,i,s=heapq.heappop(stack)
            if i==dst:
                return c
            if (i,s) in visited or s>k:
                continue
            visited[(i,s)]=1
            for j,p in neigh[i]:
                if (j,s+1) not in visited:
                    heapq.heappush(stack,[c+p,j,s+1])
        return -1



