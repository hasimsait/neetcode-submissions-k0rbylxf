class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {}
        class Node:
            def __init__(self,n):
                self.n=n
                self.pre = []
            def addPre(self,node):
                self.pre.append(node)
        for i in range(numCourses):
            courses[i]=Node(i)
        for e in prerequisites:
            courses[e[0]].addPre(courses[e[1]])
        res=[]
        def findLoop(node):
            if node.n in visited:
                return True
            if node.n in inout:
                return False
            visited.add(node.n)
            for pre in node.pre:
                if findLoop(pre):
                    return True
            visited.remove(node.n)
            inout.add(node.n)
            res.append(node.n)
            return False
        visited,inout = set(),set()
        for i in range(numCourses):
            if findLoop(courses[i]):
                return []
        return res
        
        
