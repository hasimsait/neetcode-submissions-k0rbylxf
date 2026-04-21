class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a={}
        for i in arr:
            if i not in a:
                a[i]=0
            a[i]+=1
        x=[]
        for ax in a:
            if a[ax]==1:
                x.append(ax)
        if len(x)>=k:
            return x[k-1]
        return "" 