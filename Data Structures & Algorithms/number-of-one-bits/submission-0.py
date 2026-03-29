class Solution:
    def hammingWeight(self, n: int) -> int:
        def isone(n):
            if n==0:
                return 0
            a=0
            if n%2==1:
                a = 1
            return a+isone(n>>1)
        return isone(n)