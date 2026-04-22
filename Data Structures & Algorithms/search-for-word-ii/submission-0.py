class Node:
    def __init__(self,c):
        self.ch=c
        self.children = {}
        self.eow = []
    def addChild(self,c):
        if c not in self.children:
            self.children[c]= Node(c)
        return self.children[c]
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        r = Node(' ')
        for i,w in enumerate(words):
            t=r
            for c in w:
                t=t.addChild(c)
            t.eow.append(i)
        vis = [[0 for x in r]for r in board]
        res = set()
        def findWordsFrom(start,x,y):
            if vis[x][y]==1:
                return
            vis[x][y]=1
            if len(start.eow)!=0:
                for w in start.eow:
                    res.add(w)
            for d in dirs:
                if x+d[0]>=0 and x+d[0]<len(board) and y+d[1]>=0 and y+d[1]<len(board[0]) and board[x+d[0]][y+d[1]] in start.children:
                    findWordsFrom(start.children[board[x+d[0]][y+d[1]]],x+d[0],y+d[1])
            vis[x][y]=0


        for x,row in enumerate(board):
            for y,c in enumerate(row):
                if c in r.children:
                    findWordsFrom(r.children[c],x,y)
        return [words[w] for w in res]


        