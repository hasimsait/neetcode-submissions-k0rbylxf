class Node:
    def __init__(self,c):
        self.c=c
        self.children = []
    def addChild(self,c):
        if self.children==[]:
            self.children=[Node(c)]
            return self.children[0]
        i=0
        for ch in self.children:
            if ord(ch.c)<ord(c):
                i+=1
            elif ch.c==c:
                return ch
            else:
                break
        a=Node(c)
        self.children = self.children[:i]+[a]+self.children[i:]
        return a
    def getChild(self,c):
        for i in self.children:
            if i.c==c:
                return i
        return None
class WordDictionary:

    def __init__(self):
        self.root = Node(' ')

    def addWord(self, word: str) -> None:
        r=self.root
        for c in word+" ":
            r=r.addChild(c)

    def search(self, word: str) -> bool:
        def s(root,word):
            if root is None:
                return False
            if word=="" and root.getChild(' ') is not None:
                return True
            elif word=="":
                return False        
            elif word[0]!='.':
                a= root.getChild(word[0])
                return s(a,word[1:])
            else:
                for child in root.children:
                    if s(child,word[1:]):
                        return True
                return False
        return s(self.root,word)
        
