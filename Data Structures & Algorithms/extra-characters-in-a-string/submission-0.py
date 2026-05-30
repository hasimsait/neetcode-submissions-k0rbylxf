class Node:
    def __init__(self,w):
        self.w = w
        self.c={}
    def addWord(self,w):
        if len(w)==0:
            return
        if w[0] not in self.c:
            self.c[w[0]] = Node(w[0])
        self.c[w[0]].addWord(w[1:])
class Solution:
    
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Node(' ')
        for w in dictionary:
            root.addWord(w+' ')
        mem = {len(s):0}
        def d(i):
            if i not in mem:
                r=1+d(i+1)
                c=root
                for j in range(i,len(s)):
                    if s[j] not in c.c:
                        break
                    c = c.c[s[j]]
                    if ' ' in c.c:
                        r = min(r,d(j+1))
                mem[i]=r
            return mem[i]
        return d(0)
        