class Solution:
    def minLength(self, s: str) -> int:
        while s:
            t="".join("".join(s.split("AB")).split("CD"))
            if t==s:
                return len(t)
            s=t
        return 0
            

