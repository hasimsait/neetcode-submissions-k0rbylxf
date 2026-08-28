class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s,n,mem=sum(stones),len(stones),{}
        t=s//2

        def c(i,m):
            if (i,m) in mem:
                return mem[(i,m)]
            if m>=t or i==n:
                mem[(i,m)] = abs(s-2*m)
            else:
                mem[(i,m)] = min(c(i+1,m),c(i+1,m+stones[i]))
            return mem[(i,m)]
        
        return c(0,0)

