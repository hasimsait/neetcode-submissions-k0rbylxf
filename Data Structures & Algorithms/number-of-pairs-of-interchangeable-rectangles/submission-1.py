class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        import math
        from collections import defaultdict
        a=defaultdict(int)
        for r in rectangles:
            g = math.gcd(r[0],r[1])
            ar = (r[0]//g,r[1]//g)
            a[ar]+=1
        def comb(a):
            return a*(a-1)//2
        return sum([comb(x) for x in a.values()])

