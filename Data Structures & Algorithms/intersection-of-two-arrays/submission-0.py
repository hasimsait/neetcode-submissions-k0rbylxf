class Solution:
    def intersection(self, a: List[int], b: List[int]) -> List[int]:
        if len(b)>len(a):
            a,b = b,a
        x={c:0 for c in b}
        for i in a:
            if i in x:
                x[i]=1
        r=[]
        for i in x:
            if x[i]==1:
                r.append(i)
        return r