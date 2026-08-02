class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=list(filter(lambda n: n > 0, nums))
        n=list(filter(lambda n: n < 0, nums))
        r=[]
        s=True
        while n:
            if s and p:
                r.append(p.pop(0))
            else:
                r.append(n.pop(0))
            s=not s
        return r

