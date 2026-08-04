class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        l = sum(matchsticks)/4
        matchsticks.sort()
        a=(True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True)
        for i in range(len(matchsticks),16):
            matchsticks.append(0)
        mem = {}
        def s(a,doneSides,curSideLeft):
            h = doneSides*(l+1) - curSideLeft
            if (a,h) in mem:
                return mem[(a,h)]
            if curSideLeft==0:
                if doneSides == 4:
                    return True
                mem[(a,h)] = s(a,doneSides+1,l)
                return mem[(a,h)]
            i=0
            while i<16 and matchsticks[i]<=curSideLeft:
                if a[i]:
                    an=a[:i] + (False,) + a[i+1:]
                    if s(an,doneSides,curSideLeft-matchsticks[i]):
                        return True
                i+=1
            mem[(a,h)]=False
            return False
        return s(a,0,0)
                

            
