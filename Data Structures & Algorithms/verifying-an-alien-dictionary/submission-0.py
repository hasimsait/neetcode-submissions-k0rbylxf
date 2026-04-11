class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = ' '+order
        v = {}
        for i,c in enumerate(order):
            v[c]=i
        #0 padding on left
        maxl = 0
        for w in words:
            maxl = max(len(w),maxl)
        for i,w in enumerate(words):
            words[i] = w+"".join([' ' for x in range(maxl-len(w))])
        m = len(v)+1
        vals =[]
        for word in words:
            s= 0
            st=0
            for c in word[::-1]:
                s+=v[c]*pow(m,st)
                st+=1
            vals.append(s)
        c=vals.copy()
        c.sort()
        for i in range(len(c)):
            if c[i]!=vals[i]:
                return False
        return True

