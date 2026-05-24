class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a={}
        b={}
        for i,x in enumerate(s):
            if x not in a:
                a[x]=[]
            a[x].append(i)
            b[i]=x
        for x in a:
            a[x].append(' ')
        for i,x in enumerate(t):
            l = b[i]
            if a[l][-1]==' ':
                a[l][-1] = x
            elif a[l][-1]!=x:
                return False
        x=set()
        for y in a:
            if a[y][-1] in x:
                return False
            x.add(a[y][-1])
        return True
        