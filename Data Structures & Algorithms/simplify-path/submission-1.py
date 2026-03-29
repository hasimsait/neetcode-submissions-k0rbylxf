class Solution:
    def simplifyPath(self, path: str) -> str:
        a=path.split('/')
        b=[]
        for x in a:
            if x!="":
                b.append(x)
        a=[]
        for d in b:
            if d=="..":
                a=a[:-1]
            elif d==".":
                continue
            else:
                a.append(d)
        return '/'+'/'.join(a)