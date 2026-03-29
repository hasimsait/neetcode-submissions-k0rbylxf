class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board)==0 or len(board[0])==0:
            return false
        ymax=len(board[0])
        xmax=len(board)
        i,j,ind = 0,0,0
        class Node:
            def __init__(self,x,y,v):
                self.x=x
                self.y=y
                self.v = v
        nodeByV = {}
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] not in nodeByV:
                    nodeByV[board[x][y]]=[]
                nodeByV[board[x][y]].append(Node(x,y,board[x][y]))
        if len(word)==0:
            return True
        c=word[0]
        if c not in nodeByV:
            return False
        def hc(x:int,y:int)->str:
            return str(x)+" "+str(y)
        def search(w:str, x:int,y:int,visited:str)->bool:
            if w=="":
                return True
            v=visited
            v+=hc(x,y)
            a=[]
            print(v)
            if x-1>=0 and hc(x-1,y) not in v and board[x-1][y]==w[0]:
                a.append(search(w[1:],x-1,y,v))
            if x+1<xmax and hc(x+1,y) not in v and board[x+1][y]==w[0]:
                a.append(search(w[1:],x+1,y,v))
            if y-1>=0 and hc(x,y-1) not in v and board[x][y-1]==w[0]:
                a.append(search(w[1:],x,y-1,v))
            if y+1<ymax and hc(x,y+1) not in v and board[x][y+1]==w[0]:
                a.append(search(w[1:],x,y+1,v))
            return True in a
        p=[]
        for s in nodeByV[c]:
            p.append(search(word[1:],s.x,s.y,""))
        return True in p