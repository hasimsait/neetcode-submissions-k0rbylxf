class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        opens = ['(','[','{']
        closes = ['}',']',')']
        for i,p in enumerate(s):
            if p in opens:
                a.append(p)
            elif p in closes and len(a)>0:
                if p=='}' and a[-1]=='{':
                    a=a[:-1]
                elif p==']' and a[-1]=='[':
                    a=a[:-1]
                elif p==')' and a[-1]=='(':
                    a=a[:-1]
                else:
                    return False
            else:
                return False
        return len(a)==0

