class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}
        def s(s1,s2):
            if (s1,s2) in mem:
                return mem[(s1,s2)]
            if s1==len(word1):
                a=len(word2)-s2
            elif s2==len(word2):
                a=len(word1)-s1
            elif word1[s1]==word2[s2]:
                a=s(s1+1,s2+1)
            else:
                r=s(s1+1,s2+1)
                i=s(s1,s2+1)
                d=s(s1+1,s2)
                a=min([r,i,d])+1
            mem[(s1,s2)]=a
            return a
        return s(0,0)