class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem = {}
        def s(d,hold):
            if d == len(prices):
                return 0
            if (d,hold) in mem:
                return mem[(d,hold)]
            p = s(d+1,hold) #nothing
            if hold:
                p = max(p,prices[d]+s(d+1,False)) #sell
            else:
                p = max(p,-prices[d]+s(d+1,True)) #buy
            mem[(d,hold)] = p
            return p
        return s(0,False)