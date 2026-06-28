class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def vc(w):
            a={'a', 'e', 'i', 'o', 'u'}
            if len(w)==0:
                return False
            return 1 if w[0] in a and w[-1] in a else 0
        r = [0]
        for w in words:
            r.append(r[-1]+vc(w))
        res = []
        for q in queries:
            if q[0]>q[1] or q[0]<0 or q[1]>len(words):
                res.append(-1)
            else:
                res.append(r[q[1]+1]-r[q[0]])
        return res
