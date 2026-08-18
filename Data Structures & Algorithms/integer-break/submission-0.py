class Solution:
    def integerBreak(self, n: int) -> int:
        #2 2->4
        #3 3 ->9>8
        #4 4 ->16<18
        #5 5 ->25<27<36
        #get as many 3 as possible, if %3==1, instead get 2x2
        if n<=3:
            return n-1
        pow3 = n//3 if n%3!=1 else n//3 -1
        mult = 1 if n%3!=1 else 4
        pow2 = max(1,n%3)
        return (3**pow3)*pow2*mult

