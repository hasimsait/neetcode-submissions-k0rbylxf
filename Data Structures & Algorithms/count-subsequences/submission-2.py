class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        iByV = defaultdict(list)
        for i,c in enumerate(s):
            iByV[c].append(i)
        mem={}
        def c(ifs,ift):
            if ift == len(t):
                return 1
            if ifs == len(s):
                return 0
            if (ifs,ift) in mem:
                return mem[(ifs,ift)]
            r=0
            for i in filter(lambda x: x >=ifs, iByV[t[ift]]):
                r+=c(i+1,ift+1)
            mem[(ifs,ift)] = r
            return r
        return c(0,0)
