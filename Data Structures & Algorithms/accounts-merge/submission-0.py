class Solution:
    class UnionFind:
        def __init__(self,n):
            self.p=[i for i in range(n)]
            self.r = [1]*n
        def f(self,x):
            while x!=self.p[x]:
                self.p[x]=self.p[self.p[x]]
                x=self.p[x]
            return x
        def u(self,x1,x2):
            p1,p2 = self.f(x1),self.f(x2)
            if p1==p2:
                return False
            if self.r[p1]>self.r[p2]:
                self.p[p2]=p1
                self.r[p1]+self.r[p2]
            else:
                self.p[p1]=p2
                self.r[p2]+self.r[p1]
            return True
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf= self.UnionFind(len(accounts))
        etoA = {}
        for i,a in enumerate(accounts):
            for e in a[1:]:
                if e in etoA:
                    uf.u(i,etoA[e])
                else:
                    etoA[e] = i
        eg = defaultdict(list)
        for e in etoA:
            l=uf.f(etoA[e])
            eg[l].append(e)
        r=[]
        for e in eg:
            n=accounts[e][0]
            r.append([n]+sorted(eg[e]))
        return r
