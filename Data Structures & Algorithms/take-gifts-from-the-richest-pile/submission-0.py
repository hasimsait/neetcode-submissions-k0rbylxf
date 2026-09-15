class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        g=[]
        for i in gifts:
            heapq.heappush(g,-1*i)

        for _ in range(k):
            n = -1*heapq.heappop(g)
            heapq.heappush(g, -1*floor(sqrt(n)))

        return -1*sum(g)