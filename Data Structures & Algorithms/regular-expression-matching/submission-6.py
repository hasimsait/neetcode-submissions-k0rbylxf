class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import lru_cache
        t=[]
        s+='a'
        p+='a'
        for i in p:
            if i=='*':
                t[-1]+=i
            else:
                t.append(str(i))
        @lru_cache(len(t)*len(p))
        def matchFrom(i,j):
            if i==len(s) and j==len(t):
                return True
            if j>=len(t) or i>=len(s):
                return False

            if t[j]=='.':
                return matchFrom(i+1,j+1)
            if len(t[j])==1:
                return s[i]==t[j] and matchFrom(i+1,j+1)
            
            else:
                if matchFrom(i,j+1): #c*a a. * repeats 0 times
                        return True
                if t[j][0]!='.':
                    while i<len(s) and s[i]==t[j][0]:
                        if matchFrom(i+1,j+1):
                            return True
                        i+=1
                    return False
                else:
                    while i<len(s):
                        if matchFrom(i+1,j+1):
                            return True
                        i+=1
                    return False
        return matchFrom(0,0)