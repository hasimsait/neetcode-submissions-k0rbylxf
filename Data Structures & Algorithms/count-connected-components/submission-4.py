class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        a=[[x] for x in range(n)] #every man is an island
        ad=[i for i in range(n)] #with an adress
        ct=n
        for e in edges:
            tx,ty=ad[e[0]],ad[e[1]]
            if tx!=ty:
                #if connected sink the other mans island
                #and update everyone on that islands address
                ct-=1
                for i in a[ty]:
                    ad[i]=tx
                a[tx]=a[tx]+a[ty]
        return ct