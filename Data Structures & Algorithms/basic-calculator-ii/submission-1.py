class Solution:
    def calculate(self, s: str) -> int:
        digits = {'0','1','2','3','4','5','6','7','8','9',' '}
        def getIntLeft(j:int):
            i=j
            while i>=0 and i<len(s) and s[i] in digits:
                i-=1
            return i+1
        def getIntRight(j:int):
            i=j
            while i>=0 and i<len(s) and s[i] in digits:
                i+=1
            return i-1
        s=list(s)
        for i in range(len(s)):
            if s[i] in {'*','/'}:
                l=getIntLeft(i-1)
                r=getIntRight(i+1)+1
                ln=int("".join(s[l:i]).strip())
                rn=int("".join(s[i+1:r]).strip())
                n= str(ln*rn) if s[i]=='*' else str(ln//rn)
                ct=0
                for j in range(l,r):
                    s[j]=n[ct] if ct<len(n) else ' '
                    ct+=1
        r=0
        cur=[]
        curSign=True
        print(s)
        s.append('+')
        for c in s:
            if c not in {' ','+','-'}:
                cur.append(c)
            elif c in {'+','-'}:
                if curSign:
                    r+=int("".join(cur))
                    cur=[]
                else:
                    r-=int("".join(cur))
                    cur=[]
                if c=='-':
                    curSign=False
                else:
                    curSign=True
        return r

                    

