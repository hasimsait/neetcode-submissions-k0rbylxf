class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        d=[]
        if s1==s2:
            return True
        for c in range(len(s1)):
            if s1[c]!=s2[c]:
                if len(d)==2:
                    return False
                d.append(c)
        return len(d)==2 and s1[d[0]]==s2[d[1]] and s1[d[1]]==s2[d[0]]
        

