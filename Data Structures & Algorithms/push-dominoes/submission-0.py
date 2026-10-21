class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list("L"+dominoes+"R")
        s=[]
        for i,c in enumerate(dominoes):
            if c=='.':
                if s and s[-1][-1]==i-1:
                    s[-1][-1]=i
                else:
                    s.append([i,i])     
        for l,r in s:
            while l<=r:
                if l==r:
                    if dominoes[l-1]=='R':
                        if dominoes[r+1]=='L':
                            dominoes[l]='.'
                        else:
                            dominoes[l]='R'
                    elif dominoes[r+1]=='L':
                        dominoes[r]='L'
                    l+=1
                else:
                    if dominoes[l-1]=='R':
                        dominoes[l]='R'
                        l+=1
                    if dominoes[r+1]=='L':
                        dominoes[r]='L'
                        r-=1
                    if dominoes[r+1]!='L' and dominoes[l-1]!='R':
                        l=r+1
        return "".join(dominoes)[1:-1]

