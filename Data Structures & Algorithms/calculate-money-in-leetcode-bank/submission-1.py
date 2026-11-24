class Solution:
    def totalMoney(self, n: int) -> int:
        d=[0,1,3,6,10,15, 21]
        k=n//7
        return int(k*(28 + 3.5*(k-1) + n%7)+d[n%7])
