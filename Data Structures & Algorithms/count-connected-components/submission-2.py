class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        a=[[x] for x in range(n)]
        ad=[i for i in range(n)]
        ct=n
        for e in edges:
            x,y=e[0],e[1]
            tx,ty=ad[x],ad[y]
            islandToKeep = min(tx,ty)
            islandToSink = max(tx,ty)
            if tx!=ty:
                islanders = a[islandToSink]
                n-=1
                for i in islanders:
                    ad[i]=islandToKeep
                a[islandToKeep]=a[islandToKeep]+islanders
        return n