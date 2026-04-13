class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem={}
        def c(r,i):
            if r==0:
                return 1
            if (r,i) in mem:
                return mem[(r,i)]
            if r<0:
                return 0
            s=0
            for j in range(i,len(coins)):
                s+=c(r-coins[j],j)
            mem[(r,i)]=s
            return s
        return c(amount,0)
