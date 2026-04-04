class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        x =  {}
        for a in tasks:
            if a not in x:
                x[a]=0
            x[a]+=1
        b=[[x[t],t] for t in x]
        b.sort()
        b=b[::-1]
        prio = [t[1] for t in b if t[0]==b[0][0]]
        return max(len(prio)+(b[0][0]-1)*(n+1),len(tasks))

