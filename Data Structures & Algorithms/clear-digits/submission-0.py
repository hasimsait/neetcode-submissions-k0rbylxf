class Solution:
    def clearDigits(self, s: str) -> str:
        a=[]
        for c in s:
            if c>='0' and c<='9' and a:
                a.pop()
            else:
                a.append(c)
        return "".join(a)
