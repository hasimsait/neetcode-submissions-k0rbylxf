class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < (1 << k):
            return False

        seen = [False] * (1 << k)
        c=0
        ctr=0
        for i in range(n):
            c=c<<1 & ((1<<k)-1)
            if (ord(s[i]) - ord('0')):
                c+=1
            if i>=k-1:
                if not seen[c]:
                    seen[c]=True
                    ctr+=1
        return ctr==len(seen)