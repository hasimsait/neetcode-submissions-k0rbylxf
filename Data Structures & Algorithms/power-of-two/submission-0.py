class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ct = 0
        while n>0:
            if n%2==1:
                ct+=1
                if ct==2:
                    return False
            n=n>>1
        return ct == 1