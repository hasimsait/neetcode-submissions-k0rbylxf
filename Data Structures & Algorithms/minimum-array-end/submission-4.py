class Solution:
    def minEnd(self, n: int, x: int) -> int:
        a=x
        t=n-1
        r=0
        i=0
        while t>0 or a>0:
            #is the bit occupied on either side
            usedbyx = a%2==1
            usedbyn = t%2==1
            if usedbyx:
                r+=2**i
                a=a>>1
            elif usedbyn:
                r+=2**i
                t=t>>1
                if not usedbyx:
                    a=a>>1
            else:
                a=a>>1
                t=t>>1
            i+=1
        return r