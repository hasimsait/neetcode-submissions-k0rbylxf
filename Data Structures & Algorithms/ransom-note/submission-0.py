class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=[0]*26
        for i in magazine:
            c[ord(i)-ord('a')]+=1
        for i in ransomNote:
            if c[ord(i)-ord('a')]<1:
                return False
            c[ord(i)-ord('a')]-=1
        return True
            
            