class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        t=start^goal
        c=0
        while t:
            if t&1==1:
                c+=1
            t=t>>1
        return c