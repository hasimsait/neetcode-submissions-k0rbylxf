class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a={}
        t=[]
        for p in points:
            x,y=p[0],p[1]
            d=x*x+y*y
            if d not in a:
                t.append(d)
                a[d]=[]
            a[d].append(p)
        t.sort()
        t=t[::-1]
        r=[]
        while len(r)<k and len(t)>0:
            d=k-len(r)
            m = t.pop()
            r = r+a[m]
        return r[:k]