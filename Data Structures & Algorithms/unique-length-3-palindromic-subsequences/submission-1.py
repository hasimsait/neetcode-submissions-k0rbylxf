class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        re=[0]*26
        le=[0]*26
        r=set()
        for c in s:
            re[ord(c)-ord('a')]+=1
        for c in s:
            re[ord(c)-ord('a')]-=1
            for i in range(26):
                if re[i]>0 and le[i]>0:
                    r.add(30*(ord(c)-ord('a'))+i)
            le[ord(c)-ord('a')]+=1
        return len(r)


        