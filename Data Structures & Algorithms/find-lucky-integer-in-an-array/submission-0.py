class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c=defaultdict(int)
        for i in arr:
            c[i]+=1
        r=[]
        for i in c:
            if c[i]==i:
                r.append(i)
        r.sort()
        return r[-1] if len(r)!=0 else -1