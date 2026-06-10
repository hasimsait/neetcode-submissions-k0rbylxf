class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        de = set()
        vis=set()
        self.st=[]
        for x in deadends:
            de.add(x)
        def s(a):
            c=[]
            for i in range(4):
                if a[i]=='9':
                    a1 = a[:i]+'0'+a[i+1:]
                    a2 = a[:i]+'8'+a[i+1:]
                    if a1 not in de and a1 not in vis:
                        c.append(a1)
                    if a2 not in de and a2 not in vis:
                        c.append(a2)
                elif a[i]=='0':
                    a1 = a[:i]+'1'+a[i+1:]
                    a2 = a[:i]+'9'+a[i+1:]
                    if a1 not in de and a1 not in vis:
                        c.append(a1)
                    if a2 not in de and a2 not in vis:
                        c.append(a2)
                else:
                    a1 = a[:i]+chr(ord(a[i])+1)+a[i+1:]
                    a2 = a[:i]+chr(ord(a[i])-1)+a[i+1:]
                    if a1 not in de and a1 not in vis:
                        c.append(a1)
                    if a2 not in de and a2 not in vis:
                        c.append(a2)
            return c
        
        def r():
            (a,c)=self.st.pop(0)
            if a in vis:
                return -1
            elif a in de:
                return -1
            elif a==target:
                return c
            else:
                vis.add(a)
                self.st+=[(com,c+1) for com in s(a)]
                return -1
        self.st.append(("0000",0))
        c=-1
        while len(self.st)>0 and c==-1:
            c=r()
        return c
