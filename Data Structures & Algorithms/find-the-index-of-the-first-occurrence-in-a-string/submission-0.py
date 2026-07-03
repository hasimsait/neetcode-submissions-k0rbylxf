class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            match = True
            for k in range(len(needle)):
                if i+k>=len(haystack) or haystack[i+k]!=needle[k]:
                    match=False
                    break
            if match:
                return i
        return -1