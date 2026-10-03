class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s=list(s)
        s.sort(reverse=True)
        c=0
        while c<len(s) and s[c]=='1':
            c+=1
        if c!=len(s):
            s[c-1]='0'
            s[-1]='1'
        return "".join(s)