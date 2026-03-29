class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def s(i):
            if i==0: return 0
            elif i == 1:
                return 1
            elif i == 2:
                return 2
            elif i in memo:
                return memo[i]
            else:
                memo[i] = s(i-2)+s(i-1)
                return memo[i]
        return s(n)