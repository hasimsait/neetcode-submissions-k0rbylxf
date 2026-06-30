class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = {}
        for i in range(len(username)):
            u,t,w = username[i],timestamp[i],website[i]
            if u not in visits:
                visits[u] = []
            heapq.heappush(visits[u],(t,w))
        ptrn = defaultdict(int)
        for u in visits:
            a=[]
            while len(visits[u])>0:
                if len(a)==3:
                    a.pop(0)
                a.append(heapq.heappop(visits[u])[1])
                if len(a)==3:
                    ptrn[" ".join(a)]+=1
        ss=[(-1*ptrn[x],x) for x in ptrn]
        ss.sort()
        return ss[0][1].split(' ')
                