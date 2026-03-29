class Solution:
    def mySqrt(self, x: int) -> int:
        a,s=1,True
        while pow(a,2)<=x and s:
            if pow(a,2)==x:
                return a
            a+=1
        return a-1
