class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        vis=set()
        que = [(len(t),0,0)]
        def se():
            c,i,j=heapq.heappop(que)
            if i==len(s):
                return len(t)-j
            if j==len(t):
                return 0
            if (i,j) in vis:
                return len(t)
            heapq.heappush(que,(len(t)-j,i+1,j))
            if s[i]==t[j]:
                heapq.heappush(que,(len(t)-j-1,i+1,j+1))
            vis.add((i,j))
            return len(t)
        res = len(t)
        while res==len(t) and que:
            res = se()
        return res
            
                