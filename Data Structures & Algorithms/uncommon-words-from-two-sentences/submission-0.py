class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a=defaultdict(int)
        for s in s1.split():
            a[s]+=1
        for s in s2.split():
            a[s]+=1
        r=[]
        for key in a:
            if a[key]==1:
                r.append(key)
        return r

