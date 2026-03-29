class Node:
        def __init__(self,w):
            self.w=w
            self.c=set()
            self.children =[]
        def addChild(self,w):
            if w not in self.c:
                self.children.append(Node(w))
            self.c.add(w)
        def get(self,w):
            if w not in self.c:
                return None
            else:
                for i in self.children:
                    if i.w==w:
                        return i
                return None
class PrefixTree:
    
    def __init__(self):
        self.root = Node(' ')

    def insert(self, word: str) -> None:
        word = word+" "
        c=self.root
        for l in word:
            c.addChild(l)
            c=c.get(l)

    def search(self, word: str) -> bool:
        c=self.root
        for i in word:
            c=c.get(i)
            if c is None:
                return False
        return ' ' in c.c

    def startsWith(self, prefix: str) -> bool:
        c=self.root
        for i in prefix:
            c=c.get(i)
            if c is None:
                return False
        return True
        
        