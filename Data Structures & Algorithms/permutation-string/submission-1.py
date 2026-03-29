class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        c=[0 for i in range(26)]
        t=[0 for i in range(26)]
        for i in range(len(s1)):
            c[ord(s2[i])-ord('a')]+=1
            t[ord(s1[i])-ord('a')]+=1
        if c==t:
            return True
        for i in range(1,len(s2)-len(s1)+1):
            c[ord(s2[i-1])-ord('a')]-=1
            c[ord(s2[i+len(s1)-1])-ord('a')]+=1
            if c==t:
                #print(s2[i:i+len(s1)])
                return True
        return False
        