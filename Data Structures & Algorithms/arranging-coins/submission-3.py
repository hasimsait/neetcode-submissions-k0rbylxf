class Solution:
    def arrangeCoins(self, k: int) -> int:
        #x**2+x< 2*n
        if k<=4:
            if k<3:
                return 1
            return 2
        l,r,n = 1,k//2+1,0
        while l<=r:
            m=(l+r)//2
            if (m**2)+m <= 2*k:
                l=m+1
                n=m
            else:
                r=m-1
        return n