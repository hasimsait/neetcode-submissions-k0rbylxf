class Solution:
    def reverseBits(self, n: int) -> int:
        x=0
        for i in range(32):
            x=x<<1
            if n%2==1:
                x+=1
            n=n>>1
        return x
        