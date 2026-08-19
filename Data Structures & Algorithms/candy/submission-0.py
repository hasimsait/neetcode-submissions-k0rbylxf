class Solution:
    def candy(self, ratings: List[int]) -> int:
        def get(i,l):
            if i<0 or i>=len(l):
                return -1
            return l[i]
        c,s,r=[],len(ratings),[1]*len(ratings)
        for i in range(0,len(ratings)):
            if get(i-1,ratings)<ratings[i]:
                t=r[i]
                r[i] = max(get(i-1,r)+1,t)
                s+=r[i]-t
            elif i-1>=0 and ratings[i-1]>ratings[i]:
                t=r[i-1]
                r[i-1] = max(t,r[i]+1)
                s+=r[i-1]-t
        for i in range(0,len(ratings))[::-1]:
            if get(i+1,ratings)<ratings[i]:
                t=r[i]
                r[i] = max(get(i+1,r)+1,t)
                s+=r[i]-t
            elif i+1<len(r) and ratings[i+1]>ratings[i]:
                t=r[i+1]
                r[i+1] = max(t,r[i]+1)
                s+=r[i+1]-t
        return s

