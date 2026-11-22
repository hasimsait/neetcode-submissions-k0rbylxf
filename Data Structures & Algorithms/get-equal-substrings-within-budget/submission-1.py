class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l=c=res = 0
        for r in range(len(s)):
            c+=abs(ord(s[r])-ord(t[r]))
            while c>maxCost:
                c-=abs(ord(s[l])-ord(t[l]))
                l+=1
            res = max(res,r-l+1)
        return res

