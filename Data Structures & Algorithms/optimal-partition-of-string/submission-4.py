class Solution:
    def partitionString(self, s: str) -> int:
        x=[0]*26
        m=1
        o=ord('a')
        for c in s:
            t=ord(c)-o
            if x[t]>0:
                m+=1
                x=[0]*26
            x[t]=1
        return m
