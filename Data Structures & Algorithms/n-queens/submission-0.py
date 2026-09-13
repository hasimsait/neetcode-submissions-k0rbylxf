class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #i+j
        #00
        #01 10
        #20 11 02
        #30 21 12 03
        #31 22 13
        #32 23 
        #33

        #i-j
        #03
        #02 13
        #01 12 23
        #00 11 22
        #10 21 32
        #20 31
        #30
        col=set()
        diag1 = set()
        diag2 = set()
        r = []
        b = [0]*n
        def s(i):
            if i==n:
                board = []
                for row in b:
                    rs="."*n
                    for i in range(n):
                        if row>>i==1:
                            rs="."*i+"Q"+"."*(n-i-1)
                    board.append(rs)

                r.append(board)
                return
            for c in range(n):
                if c in col or (i+c) in diag1 or (i-c) in diag2:
                    continue
                col.add(c)
                diag1.add(i+c)
                diag2.add(i-c)
                b[i]+= 2**c
                s(i+1)
                col.remove(c)
                diag1.remove(i+c)
                diag2.remove(i-c)
                b[i]=0
        s(0)
        return r
        