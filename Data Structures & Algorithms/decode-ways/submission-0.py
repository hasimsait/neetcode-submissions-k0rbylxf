class Solution:
    def numDecodings(self, s: str) -> int:
        def a(s):
            if len(s)==0:
                return 0
            if s[0]=='0':
                return 0
            if len(s)==1:
                return 1
            if len(s)==2 and int(s[:2])<=26:
                return 1+a(s[1:])
            t=0
            if len(s)>=2 and int(s[:2])<=26:
                t+=a(s[2:])
            return t+a(s[1:])
        return a(s)
                

