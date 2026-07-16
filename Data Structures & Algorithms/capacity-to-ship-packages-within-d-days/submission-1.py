class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def works(c):
            s,cc=1,c
            for w in weights:
                if cc-w<0:
                    s+=1
                    if s>days:
                        return False
                    cc=c
                cc-=w
            return True
        l,r = max(weights),sum(weights) #must be able to ship the largest load
        n=r
        while l<=r:
            c=(l+r)//2
            if works(c):
                n=c
                r=c-1
            else:
                l=c+1
        return n
