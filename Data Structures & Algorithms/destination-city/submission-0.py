class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        i,o=set(),set()
        for p in paths:
            i.add(p[0])
            o.add(p[1])
        for c in o:
            if c not in i:
                return c
        return ""
