class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n=len(s)
        a=[0]*(n+1)
        b=[0]*(n+1)
        c=[0]*(n+1)
        ps = [a,b,c]
        ind={'a':0,'b':1,'c':2}
        for i,ch in enumerate(s):
            for t in range(3):
                ps[t][i+1]=ps[t][i]
            ps[ind[ch]][i+1]+=1
        if k==0:
            return 0
        if a[-1]<k or b[-1]<k or c[-1]<k:
            return -1
        ts=[a[-1]-k,b[-1]-k,c[-1]-k]
        l,r,m = 0,0,0
        cts=[0]*3
        while r<n:
            cts[ind[s[r]]]+=1
            while cts[ind[s[r]]]>ts[ind[s[r]]]:
                cts[ind[s[l]]]-=1
                l+=1
            r+=1
            m=max(m,r-l)
        return n-m

        
            
