class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.a= [[] for j in matrix]
        for i,row in enumerate(matrix):
            csum = 0
            for j,cell in enumerate(row):
                csum+=cell
                self.a[i].append(csum)
        for j in range(len(matrix[0])):
            csum =0
            for i in range(len(matrix)):
                csum+=self.a[i][j]
                self.a[i][j]=csum
        for i in self.a:
            print(i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ex = 0
        if col1==0 and row1==0:
            return self.a[row2][col2]
        elif col1==0:
            ex = -1 * self.a[row1-1][col2]
        elif row1==0:
            ex = -1 * self.a[row2][col1-1]
        else:
            ex = -1 * self.a[row1-1][col2] + -1 * self.a[row2][col1-1] + self.a[row1-1][col1-1]
        return self.a[row2][col2]+ex
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)