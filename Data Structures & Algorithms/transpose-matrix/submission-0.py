class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix)==0:
            return []
        r=[]
        for i in range(len(matrix[0])):
            r.append([])
            for j in range(len(matrix)):
                r[-1].append(matrix[j][i])
        return r