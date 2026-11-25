class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = {p[0] for p in points}
        if len(xs)==0:
            return 0
        x=list(xs)
        x.sort()
        p=x[0]
        wm = 0
        for r in x[1:]:
            wm = max(r-p,wm)
            p=r
        return wm

