class Solution:
    def countBits(self, n: int) -> List[int]:
        def isone(n):
            if n==0:
                return 0
            if n%2==1:
                return 1+isone(n>>1)
            return isone(n>>1)
        a=[]
        for i in range(n+1):
            a.append(isone(i))
        return a