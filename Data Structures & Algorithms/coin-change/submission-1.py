class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def c(a):
            if a==0:
                return 0
            if a<0:
                return 999999
            if a in memo:
                return memo[a]
            minof=999999
            for co in coins:
                minof = min(minof,c(a-co))
            if minof==999999:
                memo[a]=999999
                return 999999
            memo[a]=minof + 1
            return memo[a]
        a=c(amount)
        return -1 if a==999999 else a