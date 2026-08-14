class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        c=0
        while s and g:
            if g[0]> s[0]:
                s.pop(0)
            else:
                s.pop(0)
                g.pop(0)
                c+=1
        return c