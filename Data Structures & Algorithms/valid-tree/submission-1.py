class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #do the union thing, when an added edge is between the nodes within the union return false
        a={}
        for i in range(n):
            b=set()
            b.add(i)
            a[i]=b
        for edge in edges:
            adja=a[edge[0]]
            adjb=a[edge[1]]
            if edge[1] in adja:
                return False
            union=adja.union(adjb)
            for x in union:
                a[x]=union
        if len(a[0])==n:
            return True
        return False

