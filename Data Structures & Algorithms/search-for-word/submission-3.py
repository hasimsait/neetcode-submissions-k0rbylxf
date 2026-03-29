class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board)==0 or len(board[0])==0:
            return false
        ymax=len(board[0])
        xmax=len(board)
        i,j,ind = 0,0,0
        if len(word)==0:
            return True
        c=word[0]
        def hc(x:int,y:int)->str:
            return str(x)+" "+str(y)
        def search(w:str, x:int,y:int,visited:str)->bool:
            if w=="":
                return True
            v=visited
            v+=hc(x,y)
            a=False
            if x-1>=0 and hc(x-1,y) not in v and board[x-1][y]==w[0]:
                a= a or search(w[1:],x-1,y,v)
            if x+1<xmax and hc(x+1,y) not in v and board[x+1][y]==w[0]:
                a = a or search(w[1:],x+1,y,v)
            if y-1>=0 and hc(x,y-1) not in v and board[x][y-1]==w[0]:
                a = a or search(w[1:],x,y-1,v)
            if y+1<ymax and hc(x,y+1) not in v and board[x][y+1]==w[0]:
                a= a or search(w[1:],x,y+1,v)
            return a
        p=False
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y]==word[0]:
                    p = p or search(word[1:],x,y,"")
        return p