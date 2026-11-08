class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        a=[0]
        b=[0]
        for h in customers:
            if h=='N':
                a.append(a[-1]+1)
            else:
                a.append(a[-1])
        for h in customers[::-1]:
            if h=='N':
                b.append(b[-1])
            else:
                b.append(b[-1]+1)
        b=b[::-1]
        m=float('inf')
        mi=-1
        for i in range(n+1):
            if a[i]+b[i]<m:
                mi=i
                m=a[i]+b[i]
        return mi
