class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = []
        adj = [[False] * numCourses for i in range(numCourses)]

        for p, c in prerequisites:
            adj[p][c] = True

        for k in range(numCourses):#n hop at most
            for i in range(numCourses):
                for j in range(numCourses):
                    adj[i][j] = adj[i][j] or (adj[i][k] and adj[k][j])

        return [adj[q[0]][q[1]] for q in queries]