class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        class Node:
            def __init__(self,c):
                self.c = c
                self.ch = [None]*26
                self.ct = 0
                self.chids = []
            def addCh(self,c,id):
                if len(self.chids)<3:
                    self.chids.append(id)
                if not self.ch[ord(c)-ord('a')]:
                    self.ch[ord(c)-ord('a')]=Node(c)
                    self.ct+=1
                return self.ch[ord(c)-ord('a')]
            def collapse(self):
                for i in range(26):
                    if self.ch[i]:
                        self.ch[i].collapse()
                        if self.ct==1 and self.chids == self.ch[i].chids:
                            self.c = self.c+self.ch[i].c
                            self.ct = self.ch[i].ct
                            self.ch=self.ch[i].ch
                            return
            def getSuggested(self):
                return [products[x] for x in self.chids]
            def find(self, c):
                if self.c:
                    if self.c[0] == c:
                        self.c = self.c[1:]
                        return self
                    return None
                if self.ch[ord(c) - ord('a')]:
                    self.ch[ord(c) - ord('a')].c = self.ch[ord(c) - ord('a')].c[1:]
                return self.ch[ord(c) - ord('a')]
        h=Node("")
        for i,p in enumerate(products):
            t=h
            for c in p:
                t=t.addCh(c,i)
            t.addCh("a",i)
        #h.collapse()
        r=[[] for _ in range(len(searchWord))]
        for i,c in enumerate(searchWord):
            h=h.find(c)
            if not h:
                break
            r[i]=h.getSuggested()

        return r


                


