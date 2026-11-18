class Solution:
    def shortestPalindrome(self, s: str) -> str:
        m=len(s)//2
        t=""
        for i in range(len(s)):
            if t+s==s[::-1]+t[::-1]:
                return t+s
            t=t+s[-len(t)-1]
        return s+s[::-1]