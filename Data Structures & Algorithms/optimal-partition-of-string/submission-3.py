class Solution:
    def partitionString(self, s: str) -> int:
        x=[0]*26
        m=0
        for c in s:
            if x[ord(c)-ord('a')]>0:
                m+=1
                for i in range(26):
                    x[i]=0
            x[ord(c)-ord('a')]=1
        return m+1
