class Solution:
    def largestGoodInteger(self, s: str) -> str:
        m=-1
        i=0
        while i<=len(s)-3:
            if s[i+1]==s[i+2]:
                if s[i]==s[i+1]:
                    m=max(ord(s[i]),m)
                    i+=3
                else:
                    i+=1
            else:
                i+=2
        return chr(m)*3 if m!=-1 else ""
            