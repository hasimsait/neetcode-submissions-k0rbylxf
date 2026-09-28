class Solution:
    def maxDepth(self, s: str) -> int:
        m,ct=0,0
        for c in s:
            if c=='(':
                ct+=1
                m=max(ct,m)
            elif c==')':
                ct-=1
        return m