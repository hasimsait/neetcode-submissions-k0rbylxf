class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res=[]
        for s in spells:
            l,r,n=0,len(potions)-1,len(potions)
            while l<=r:
                m=(l+r)//2
                if potions[m]*s>=success:
                    n=m
                    r=m-1
                else:
                    l=m+1
            res.append(len(potions)-n)
        return res
