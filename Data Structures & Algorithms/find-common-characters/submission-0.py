class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = defaultdict(int)
        for c in words[0]:
            common[c]+=1
        for w in words:
            t=common.copy()
            for c in w:
                if c in t:
                    t[c]-=1
            for c in t:
                common[c]-=max(0,t[c])
        r=[]
        for c in common:
            for t in range(common[c]):
                r.append(c)
        return r
