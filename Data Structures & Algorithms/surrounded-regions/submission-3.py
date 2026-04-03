class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dire = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = [[0 for i in board[0]] for x in board]
        def dfs(i,j):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False
            elif board[i][j]=="X":
                return True
            elif visited[i][j]!=0:
                return visited[i][j] == 1
            else:
                visited[i][j]=1
                a = True
                for d in dire:
                    res = dfs(i+d[0],j+d[1])
                    a = a and res
                if not a:
                    visited[i][j]=2
                return a
        def sink(i,j):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]=="X":
                return
            board[i][j]="X"
            for d in dire:
                sink(i+d[0],j+d[1])
        for i,row in enumerate(board):
            for j,cell in enumerate(row):
                if cell == "O" and visited[i][j] == 0:
                    if dfs(i,j):
                        sink(i,j)