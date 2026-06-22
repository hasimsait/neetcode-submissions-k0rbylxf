class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wtimes = []
        ctime = 0
        for c in customers:
            ctime = max(ctime,c[0])+c[1]
            wtimes.append(ctime-c[0])
        return sum(wtimes)/len(wtimes)
        
