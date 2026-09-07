class Solution:
    def numSquares(self, n: int) -> int:
        mem = {0:0,1:1}
        def d(i):
            if i in mem:
                return mem[i]
            r=i
            for j in range(1,int(math.sqrt(i))+1)[::-1]:
                if j**2>i:
                    continue
                r=min(r,1+d(i-j**2))
            mem[i]=r
            return r
        return d(n)
                