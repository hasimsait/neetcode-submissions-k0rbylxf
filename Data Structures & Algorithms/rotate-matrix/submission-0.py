class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        t=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for r in range(len(matrix)):
            matrix[r]=t[r][::-1]
