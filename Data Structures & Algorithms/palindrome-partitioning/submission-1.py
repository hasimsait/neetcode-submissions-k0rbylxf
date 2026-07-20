class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #todo memoization for (cursor,p[-1])
        #"aba" "a" ->"aa","a""a"
        #"a""b""a"a"->just get the existing combinations
        self.part=[]
        def palindrome(l):
            for c in l:
                if c[:(len(c)+1)//2]!=c[(len(c))//2:][::-1]:
                    return False
            return True
        def pr(c,p):
            if c==len(s):
                if palindrome(p):
                    self.part.append(p.copy())
                return
            p[-1]=p[-1]+s[c]
            pr(c+1,p)
            p[-1]=p[-1][:-1]
            p.append(s[c])
            pr(c+1,p)
            p.pop()
            return
        pr(1,[s[0]])
        return self.part