class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ibyp = {p:i for i,p in enumerate(position)}
        position.sort()
        #if youre behind someone yet reach target in a shorter time than them, no you dont.
        t=[]
        for i,p in enumerate(position[::-1]):
            t.append((target-p)/speed[ibyp[p]])
        for i,x in enumerate(t):
            if i>0:
                t[i]=max(t[i-1],t[i])
        print(position)
        print(t)
        x={a:0 for a in t}.keys()
        return len(x)


        