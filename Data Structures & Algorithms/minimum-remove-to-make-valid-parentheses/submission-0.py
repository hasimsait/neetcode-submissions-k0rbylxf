class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ct = []
        re = set()
        r= ""
        for i,c in enumerate(s):
            if c==')':
                if len(ct)==0:
                    re.add(i)
                else:
                    ct.pop()
            elif c== '(':
                ct.append(i)
        ct = {x for x in ct}
        for i,c in enumerate(s):
            if not(i in ct or i in re):
                r+=c
            
        return r
            
        