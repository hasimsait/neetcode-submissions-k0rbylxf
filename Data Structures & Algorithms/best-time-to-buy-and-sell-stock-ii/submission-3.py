class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(maxsize = 60000)
        def s(holding,day):
            if day==len(prices):
                return 0
            a=s(holding,day+1)
            if holding:
                a=max(a,s(not holding,day+1)+prices[day])
            else:
                a=max(a,s(not holding,day+1)-prices[day])
            return a
        return s(False,0)