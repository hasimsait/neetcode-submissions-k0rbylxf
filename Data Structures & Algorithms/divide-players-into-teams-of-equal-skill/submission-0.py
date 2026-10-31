class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        a=defaultdict(int)
        ct=0
        for s in skill:
            a[s]+=1
            ct+=s
        t=ct*2//len(skill)
        res =0
        for s in skill:
            a[t-s]-=1
            if a[t-s]<0:
                return -1
            res+=s*(t-s)
        return res//2