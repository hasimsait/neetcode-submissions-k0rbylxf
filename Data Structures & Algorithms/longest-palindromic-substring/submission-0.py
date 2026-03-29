class Solution:
    def longestPalindrome(self, s: str) -> str:
        lengthmax=""
        for i,c in enumerate(s):
            if i+1<len(s) and s[i+1]==c:
                #check even palindrome
                a=i-1
                b=i+2
                while a>=0 and b<len(s) and s[a]==s[b]:
                    a-=1
                    b+=1
                t=s[a+1:b]
                if len(t)>len(lengthmax):
                    #print(a,b)
                    lengthmax=t
            a=i-1
            b=i+1
            while a>=0 and b<len(s) and s[a]==s[b]:
                a-=1
                b+=1
            t=s[a+1:b]
            if len(t)>len(lengthmax):
                #print(a,b)
                lengthmax=t
        return lengthmax