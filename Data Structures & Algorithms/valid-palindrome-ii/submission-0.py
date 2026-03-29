class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(sa):
            m=len(sa)//2
            if len(sa)%2==0:
                return sa[0:m]==sa[m:][::-1]
            return sa[0:m]==sa[m+1::][::-1]
        if isPalindrome(s):
            return True
        for i in range(len(s)):
            if i==0:
                if isPalindrome(s[1:]):
                    return True
            elif i==len(s)-1:
                if isPalindrome(s[:-1]):
                    return True
            else:
                if isPalindrome(s[:i]+s[i+1:]):
                    return True
        return False