class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r,m=0,0,0
        e={}
        while r<len(fruits):
            if fruits[r] not in e and len(e)==2:
                while l<r:
                    e[fruits[l]]-=1
                    l+=1
                    if e[fruits[l-1]]==0:
                        del e[fruits[l-1]]
                        break
            if fruits[r] not in e:
                e[fruits[r]]=0
            e[fruits[r]]+=1
            s=0
            for c in e:
                s+=e[c]
            m=max(m,s)
            r+=1
        return m