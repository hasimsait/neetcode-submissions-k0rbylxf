class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for i in edges:
            nodes.add(i[0])
            nodes.add(i[1])
        a=[[x] for x in nodes]
        def findInA(node):
            for i,island in enumerate(a):
                if node in island:
                    return i
            return -1
        for e in edges:
            x=findInA(e[0])
            y=findInA(e[1])
            if x==y:
                return e
            elif x!=-1 and y!=-1:
                a[x]=a[y]+a[x]
                a[y]=[]
            else:
                return -1