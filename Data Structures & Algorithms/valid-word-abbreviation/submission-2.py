class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        s=[]
        def isDigit(c):
            return ord(c)>=ord('0') and ord(c)<=ord('9')
        for c in abbr:
            if isDigit(c):
                if len(s)>0 and isDigit(s[-1][-1]):
                    s[-1]+=c
                else:
                    if c=='0':
                        return False
                    s.append(str(c))
            else:
                s.append(str(c))
        for i,e in enumerate(s):
            if isDigit(e[0]):
                s[i]=int(s[i])
        i,j=0,0
        while i<len(word) and j<len(s):
            if isinstance(s[j],int):
                i+=s[j]
                j+=1
            else:
                if word[i]!=s[j]:
                    return False
                else:
                    i+=1
                    j+=1
        return i==len(word) and j==len(s)
