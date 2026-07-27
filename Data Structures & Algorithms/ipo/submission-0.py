class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(capital)
        j,m,p = [],[],0
        for i in range(n):
            heapq.heappush(j,(capital[i],-1*profits[i]))
        cp=0
        for i in range(k):
            while j:
                a=heapq.heappop(j)
                if a[0]<=w:
                    heapq.heappush(m,a[1])
                else:
                    heapq.heappush(j,a)
                    break
            if len(m)==0:
                break
            w+=-heapq.heappop(m)
        return w