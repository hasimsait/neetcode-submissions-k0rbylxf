class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def t(s):
            i=0
            for p in piles:
                i+=math.ceil(p/s)
            return i
        piles.sort()
        #at speed piles[-1], it would take piles.length
        #speed is less than piles[-1] since piles.length<h by a factor of 10^3
        i,j=1,piles[-1]
        res = piles[-1]
        while i<=j:
            m=(i+j)//2
            ts=t(m)
            #if ts==h:
            #    return m
            if ts<=h:
                res =m
                j=m-1
            else:
                i=m+1
        return res
        
            
