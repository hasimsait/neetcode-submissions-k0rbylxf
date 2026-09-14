class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        d1=set()
        d2=set()
        self.ans=0
        def s(r):
            if r==n:
                self.ans+=1
            for c in range(n):
                if c in col or c+r in d1 or c-r in d2:
                    continue
                col.add(c)
                d1.add(c+r)
                d2.add(c-r)
                s(r+1)
                col.remove(c)
                d1.remove(c+r)
                d2.remove(c-r)
        s(0)
        return self.ans
