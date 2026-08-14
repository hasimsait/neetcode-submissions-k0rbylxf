class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        c=0
        sp=0
        gp=0
        while sp<len(s) and gp<len(g):
            if g[gp]> s[sp]:
                sp+=1
            else:
                sp+=1
                gp+=1
                c+=1
        return c