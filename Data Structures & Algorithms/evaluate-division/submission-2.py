class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        class Gr:
            def __init__(self):
                self.n = {}
            def connect(self,a,b,w,vis):
                if a in vis:
                    return
                if a not in self.n:
                    self.n[a]={}
                self.n[a][b]=w
                vis.add(a)
                vis.add(b)
                for c in self.n[a]:
                    self.connect(c,b,w/self.n[a][c],vis)
            def find(self,a,b,vis):
                if a not in self.n:
                    return -1.0
                if b in self.n[a]:
                    return self.n[a][b]
                if a in vis:
                    return -1.0
                vis.add(a)
                for c in self.n[a]:
                    k=self.find(c,b,vis)
                    if k!=-1.0:
                        return self.n[a][c]*k
                return -1.0
        a=Gr()
        n=len(equations)
        for i in range(n):
            a.connect(equations[i][0],equations[i][1],values[i],set())
            a.connect(equations[i][1],equations[i][0],1/values[i],set())
        r=[]
        for q in queries:
            r.append(a.find(q[0],q[1],set()))
        return r


                    