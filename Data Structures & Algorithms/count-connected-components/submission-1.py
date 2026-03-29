class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        a=[[x] for x in range(n)]
        for e in edges:
            x,y=e[0],e[1]
            tx,ty=-1,-1
            for i,island in enumerate(a):
                if x in island:
                    tx= i
                if y in island:
                    ty = i
                if tx!=-1 and ty!=-1:
                    break
            islandToKeep = min(tx,ty)
            islandToSink = max(tx,ty)
            if tx!=ty:
                islanders = a[islandToSink]
                del a[islandToSink]
                a[islandToKeep]=a[islandToKeep]+islanders
        return len(a)