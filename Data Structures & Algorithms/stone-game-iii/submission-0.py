class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        mem = {}
        def s(i):
            if i>=len(stoneValue):
                return 0
            if i in mem:
                return mem[i]
            r,t = -9999999,0
            for j in range(i,min(i+3,len(stoneValue))):
                t+=stoneValue[j]
                r=max(r,t-s(j+1))
            mem[i]=r
            return r
        r=s(0)
        if r==0:
            return "Tie"
        if r>0:
            return "Alice"
        return "Bob"