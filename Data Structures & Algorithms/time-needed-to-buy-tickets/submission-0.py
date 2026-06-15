class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        c,t=0,tickets[k]
        for i,p in enumerate(tickets):
            if i<=k:
                c+=min(p,t)
            else:
                c+=min(p,t-1)
        return c