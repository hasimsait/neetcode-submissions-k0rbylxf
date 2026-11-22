class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l=c=res = 0
        d= [abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
        for r in range(len(s)):
            c+=d[r]
            while c>maxCost:
                c-=d[l]
                l+=1
            res = max(res,r-l+1)
        return res

