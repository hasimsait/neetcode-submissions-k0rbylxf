class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem={}
        def s(holding,day):
            if (holding,day) in mem:
                return mem[(holding,day)]
            if day==len(prices):
                return 0
            a=s(holding,day+1)
            if holding:
                a=max(a,s(not holding,day+1)+prices[day])
            else:
                a=max(a,s(not holding,day+1)-prices[day])
            mem[(holding,day)]=a
            return a
        return s(False,0)