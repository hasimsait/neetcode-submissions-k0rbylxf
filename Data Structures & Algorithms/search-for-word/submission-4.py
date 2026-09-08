class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        starts = []
        vis=set()
        for i,row in enumerate(board):
            for j,cell in enumerate(row):
                if cell==word[0]:
                    starts.append((i,j))
        def s(px,py,i):
            if i==len(word):
                return True
            for dx,dy in directions:
                xn,yn=px+dx,py+dy
                if (xn,yn) not in vis and xn>=0 and xn<len(board) and yn>=0 and yn<len(board[0]) and board[xn][yn]==word[i]:
                    vis.add((xn,yn))
                    if s(xn,yn,i+1):
                        return True
                    vis.remove((xn,yn))
            return False
        for sx,sy in starts:
            vis.add((sx,sy))
            if s(sx,sy,1):
                return True
            vis.remove((sx,sy))
        return False



