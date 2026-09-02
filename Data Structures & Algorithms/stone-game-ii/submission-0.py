class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        mem = {}
        def s(i,m):
            if i>=len(piles)-1:
                return 0
            if (i,m) in mem:
                return mem[(i,m)]
            c=0
            score=float('-inf')
            for j in range(1,2*m+1):
                if i+j>=len(piles):
                    break
                c+=piles[i+j]
                score=max(score,c-s(i+j,max(m,j)))
            mem[(i,m)]=score
            return score
        return (sum(piles)+s(-1,1))//2

