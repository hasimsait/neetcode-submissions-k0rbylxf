class Solution:
    def reorganizeString(self, s: str) -> str:
        c= defaultdict(int)
        for x in s:
            c[x]+=1
        a=[]
        for ch in c:
            heapq.heappush(a,(-1*c[ch],ch))
        n=len(s)
        r=" "
        while len(r)<=n:
            c=r[-1]
            t=heapq.heappop(a)
            if t[1]==c:
                if len(a)>0:
                    tt=heapq.heappop(a)
                    heapq.heappush(a,t)
                    t=tt
                else:
                    return ""
            r+=t[1]
            if t[0]<-1:
                heapq.heappush(a,(t[0]+1,t[1]))
        return r[1:]


