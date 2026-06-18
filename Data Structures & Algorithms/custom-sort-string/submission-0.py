class Solution:
    def customSortString(self, order: str, s: str) -> str:
        vbc = {}
        cbv = {}
        s=list(s)
        for i,c in enumerate(order):
            vbc[c] = i
            cbv[i] = c
        for i in range(len(s)):
            if s[i] in vbc:
                s[i]=vbc[s[i]]
            else:
                s[i] = ord(s[i]) + ord('z')
        s.sort()
        for i in range(len(s)):
            if s[i] in cbv:
                s[i]=cbv[s[i]]
            else:
                s[i] = chr(s[i]-ord('z'))
        return "".join(s)


