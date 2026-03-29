class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ibyp = {p:i for i,p in enumerate(position)}
        position.sort()
        #if youre behind someone yet reach target in a shorter time than them, no you dont.
        t=[]
        for i,p in enumerate(position[::-1]):
            t.append((target-p)/speed[ibyp[p]])
        c=1
        for i,x in enumerate(t):
            if i>0:
                if t[i-1]<t[i]:
                    c+=1
                t[i]=max(t[i-1],t[i])
        return c


        