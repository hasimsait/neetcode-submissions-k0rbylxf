class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        for i in range(len(mat)):
            s+=mat[i][i]
            s+=mat[i][-i-1]
            if len(mat)-i-1==i:
                s-=mat[i][i]
        return s