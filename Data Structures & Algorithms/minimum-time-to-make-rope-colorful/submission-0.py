class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        a=[[None,0,0]]
        for i,x in enumerate(colors):
            if x==a[-1][0]:
                a[-1][1]+=neededTime[i]
                a[-1][2]=max(a[-1][2],neededTime[i])
            else:
                a.append([x,neededTime[i],neededTime[i]])
        s=0
        for e in a:
            if e[2]!=e[1]:
                s+=e[1]-e[2]
        return s
