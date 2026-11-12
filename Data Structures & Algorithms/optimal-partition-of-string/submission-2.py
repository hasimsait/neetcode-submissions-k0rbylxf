class Solution:
    def partitionString(self, s: str) -> int:
        x=set()
        m=0
        for c in s:
            if c in x:
                m+=1
                x={c}
            else:
                x.add(c)
        return m+1
