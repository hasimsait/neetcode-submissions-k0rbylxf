class Solution:
    def longestPalindrome(self, s: str) -> int:
        a=defaultdict(int)
        for c in s:
            a[c]+=1
        hasOne = False
        s=0
        for c in a:
            if a[c]%2==1:
                hasOne = True
            s+=a[c]//2
        return s*2+1 if hasOne else s*2
            
