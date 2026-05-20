class Solution:
    def isPathCrossing(self, path: str) -> bool:
        a=defaultdict(int)
        for x in path:
            a[x]+=1
        md = 0
        for x in a:
            md = max(a[x],md)
        r = [0]*(2*md+1)
        gr=[]
        for i in range(2*md+1):
            gr.append(r.copy())
        st = [md,md]
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        for a in path:
            if gr[st[0]][st[1]]!=0:
                return True
            gr[st[0]][st[1]]=1
            if a=='N':
                st[0]+=1
            elif a=='S':
                st[0]-=1
            elif a=='E':
                st[1]+=1
            elif a=='W':
                st[1]-=1
        return gr[st[0]][st[1]]!=0