class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+2-low)//2 + (-1 if low%2==0 and high%2==0 else 0)