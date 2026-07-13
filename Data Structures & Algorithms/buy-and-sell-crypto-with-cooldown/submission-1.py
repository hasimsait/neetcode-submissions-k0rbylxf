class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem={}
        def p(holding,lastSold,day):
            if (holding,lastSold,day) in mem:
                return mem[(holding,lastSold,day)]
            if day==len(prices):
                return 0
            if holding:
                mem[(holding,lastSold,day)] = max (p(False,day,day+1)+prices[day], p(True,lastSold,day+1))
            else:
                if lastSold<day-1:
                    mem[(holding,lastSold,day)] = max(p(True,lastSold,day+1)-prices[day], p(False,lastSold,day+1))
                else:
                    mem[(holding,lastSold,day)] = p(False,lastSold,day+1)
            return mem[(holding,lastSold,day)]
        return p(False,-2,0)