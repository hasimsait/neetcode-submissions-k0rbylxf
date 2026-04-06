class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def s(a,b,c):
            x=int(a[-1]) if len(a)>0 else 0
            y=int(b[-1]) if len(b)>0 else 0
            t = x^y^c
            cn  = 1 if (x==1 and y==1) or (x==1 and c==1) or (y==1 and c==1) else 0
            if len(a)==0 and len(b)==0:
                return str(t)
            return s(a[:-1],b[:-1],cn)+str(t)
        r= s(a,b,0)
        t=r.find('1')
        return "0" if t==-1 else r[t:]
            
