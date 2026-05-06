class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = [ (x[1],x[2],x[0]) for x in trips]
        trips.sort()
        c=[]
        cap = capacity
        for i,t in enumerate(trips):
            while len(c)>0:
                firstEndTrip = heapq.heappop(c)
                if firstEndTrip[0]>t[0]:
                    heapq.heappush(c,firstEndTrip)
                    break
                else:
                    cap+=firstEndTrip[1]
            cap-=t[2]
            if cap<0:
                return False
            heapq.heappush(c,(t[1],t[2]))
        return True