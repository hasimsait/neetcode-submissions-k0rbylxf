class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        pc=[0]*26
        for c in p:
            pc[ord(c)-ord('a')]+=1
        lp=len(p)
        def m(arr):
            for i in range(26):
                if arr[i]!=0:
                    return False
            return True
        for i in range(lp-1):
            pc[ord(s[i])-ord('a')]-=1
        res = []
        for i in range(lp-1,len(s)):
            if i>=lp:
                pc[ord(s[i-lp])-ord('a')]+=1
            pc[ord(s[i])-ord('a')]-=1
            if m(pc):
                res.append(i-lp+1)
        return res
