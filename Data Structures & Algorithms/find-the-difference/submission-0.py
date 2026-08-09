class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=[0]*26
        for c in range(len(s)):
            a[ord(s[c])-ord('a')]-=1
            a[ord(t[c])-ord('a')]+=1
        a[ord(t[-1])-ord('a')]+=1
        for c in range(26):
            if a[c]:
                return chr(c+ord('a'))
        return ""
        