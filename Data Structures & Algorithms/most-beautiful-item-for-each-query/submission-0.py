class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        a=[(x[0],-x[1]) for x in items]
        a.sort()
        items = [(a[0][0],-a[0][1])]
        for pr,b in a[1:]:
            if -b>items[-1][1]:#discard more expensive yet uglier pieces
                items.append((pr,-b))
        def bs(budget):
            if budget<items[0][0]:
                return 0
            l,r,n = 0,len(items)-1,0
            while l<=r:
                m=(l+r)>>1
                if items[m][0]<=budget:
                    n=m
                    l=m+1
                else:
                    r=m-1
            return items[n][1]
        del a
        return [bs(x) for x in queries]

