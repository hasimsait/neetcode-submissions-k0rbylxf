class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRowZero=False
        firstColZero=False
        zeroRow = [0 for x in matrix[0]]
        for i,row in enumerate(matrix):
            for j,cell in enumerate(row):
                if cell == 0:
                    if i==0:
                        firstRowZero = True
                    if j==0:
                        firstColZero = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for j in range(1,len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j]=0
        for i in range(1,len(matrix)):
            if matrix[i][0]==0:
                matrix[i]=zeroRow
        if firstRowZero:
            matrix[0] = zeroRow
        if firstColZero:
            for i in range(len(matrix)):
                matrix[i][0]=0

        