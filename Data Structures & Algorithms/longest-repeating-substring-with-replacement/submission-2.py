class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        m=0
        for ss in chars:
            a=0
            while a<len(s):
                mt=0
                e=0
                kt=k
                while (a+e)<len(s) and kt>=0:
                    if s[a+e]!=ss:
                        kt-=1
                    if kt>=0:
                        mt+=1
                    e+=1
                m=max(mt,m)
                if m == len(s): return m
                a+=1
        return m
