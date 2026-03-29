class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        def conn(n):
            i=n[0]
            j=n[1]
            if j==i:
                return False
            graph[i].append(j)
            #print(graph)
            s=True
            for a in graph[j]:
                s=s and conn([i,a])
            return s
        for edge in prerequisites:
            if conn(edge)==False:
                return False
        return True
            
