class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        a=money - sum(prices[:2])
        return a if a>=0 else money