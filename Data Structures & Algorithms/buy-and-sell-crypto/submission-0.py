class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        m = []
        cmax=0
        for j in range(len(prices)):
            i = len(prices)-j-1
            cmax = max(cmax,prices[i])
            m.append(cmax)
        m=m[::-1]
        cmax = 0
        for i,n in enumerate(prices):
            cmax = max(cmax,(m[i]-prices[i]))
        return max(0,cmax)