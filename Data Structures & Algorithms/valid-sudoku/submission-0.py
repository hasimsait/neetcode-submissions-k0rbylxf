class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def nthSquare(x,y):
            return (int(x/3)*3+int(y/3))
        sq=[set() for s in range(9)]
        r=[set() for s in range(9)]
        c=[set() for s in range(9)]
        for i,row in enumerate(board):
            for j,cell in enumerate(row):
                s=nthSquare(i,j)
                if cell!="." and (cell in sq[s] or cell in r[i] or cell in c[j]):
                    return False
                sq[s].add(cell)
                r[i].add(cell)
                c[j].add(cell)
        return True

        