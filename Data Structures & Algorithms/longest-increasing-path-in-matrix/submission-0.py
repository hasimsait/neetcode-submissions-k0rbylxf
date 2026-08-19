class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        n,m = len(matrix),len(matrix[0])
        def get(i,j):
            return -1 if i<0 or i>=n or j<0 or j>=m else matrix[i][j]
        mem = {}
        def s(i,j):
            if get(i,j)==-1:
                return 0
            if (i,j) in mem:
                return mem[(i,j)]
            pmax = 1
            for d in directions:
                if get(i+d[0],j+d[1])>get(i,j):
                    pmax = max(s(i+d[0],j+d[1])+1,pmax)
            mem[(i,j)] = pmax
            return pmax
        gmax = 1
        for i in range(n):
            for j in range(m):
                gmax = max(s(i,j),gmax)
        return gmax

