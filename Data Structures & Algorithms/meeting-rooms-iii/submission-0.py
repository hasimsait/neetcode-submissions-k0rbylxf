class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        a=[0]*n
        t=0
        m = []
        rooms=[0]*n
        curtime = 0
        for i,j in meetings:
            heapq.heappush(m,(i,j-i))
        while m:
            i,d=heapq.heappop(m)
            i=max(curtime,i)
            mintime = 500001
            minroom = n+1
            placed = False
            for j in range(len(rooms)):
                if rooms[j]<mintime:
                    mintime = rooms[j]
                    minroom = j
                if rooms[j]<=i:
                    a[j]+=1
                    rooms[j] = i+d
                    placed =True
                    break
            if not placed:
                curtime = mintime
                rooms[minroom]=mintime+d
                a[minroom]+=1
        return a.index(max(a))