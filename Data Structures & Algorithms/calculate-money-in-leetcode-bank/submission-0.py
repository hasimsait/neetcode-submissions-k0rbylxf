class Solution:
    def totalMoney(self, n: int) -> int:
        d=[0,1,3,6,10,15, 21]
        return (n//7)*28 + 7*(((n-7)//7)*(n//7))//2 + (n//7)*(n%7) + d[n%7]
