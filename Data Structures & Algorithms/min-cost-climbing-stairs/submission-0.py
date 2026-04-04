class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        x=[]
        for i,step in enumerate(cost):
            if i<1:
                x.append(step)
            elif i==1:
                x.append(min(step+x[0],step))
            else:
                skipped =x[-2]
                p =x[-1]
                x.append(min(skipped,p)+step)
        return min(x[-2],x[-1])