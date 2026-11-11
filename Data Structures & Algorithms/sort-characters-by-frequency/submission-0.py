class Solution:
    def frequencySort(self, s: str) -> str:
        a=defaultdict(int)
        for c in s:
            a[c]+=1
        ct = [(a[i],i) for i in a]
        ct.sort(reverse=True)
        r=[]
        for c,d in ct:
            for _ in range(c):
                r.append(d)
        return "".join(r)
