class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res= [0]
        z = len(temperatures)
        ts = [[temperatures[-1],z-1]]
        iters = [i for i in range(z-1)][::-1]
        for x in iters:
            i = temperatures[x]
            if i>=ts[-1][0]:
                res.append(0)
                ts = [[i,x]]
            else:
                l,r,n = 0,len(ts)-1,len(ts)-1
                while l<=r:
                    m = (l+r)//2
                    if ts[m][0]>i:
                        n=m
                        r=m-1
                    else:
                        l=m+1
                res.append(ts[n][1]-x)
                ts= [[i,x]]+ts[n:]
        return res[::-1]