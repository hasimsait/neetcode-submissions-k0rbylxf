class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 1,num
        while l<=r:
            m= (l+r)//2
            s = m*m
            if s==num:
                return True
            if s>num:
                r=m-1
            else:
                l=m+1
        return False
            