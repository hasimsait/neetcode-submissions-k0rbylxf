class Solution:
    def myPow(self, x: float, n: int) -> float:
        def p(cur,times,by):
            if times == 0:
                return 1
            elif times==1:
                return cur
            else:
                return p(cur*by,times-1,by)
        if n<0:
            x=1/x
            n=-1*n
        return p(x,n,x)