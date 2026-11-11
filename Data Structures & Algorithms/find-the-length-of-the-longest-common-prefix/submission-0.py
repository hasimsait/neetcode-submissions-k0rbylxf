class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        class Trie:
            def __init__(self,d):
                self.d=d
                self.ch = [None]*10
            def add(self,d):
                if self.ch[d] is None:
                    self.ch[d]=Trie(d)
                return self.ch[d]
        t1,t2 = Trie(0),Trie(0)
        for n in arr1:
            t=[int(d) for d in str(n)]
            tn=t1
            for d in t:
                tn = tn.add(d)
        for n in arr2:
            t=[int(d) for d in str(n)]
            tn=t2
            for d in t:
                tn = tn.add(d)
        m=0
        s=deque()
        s.append((t1,t2,0))
        while s:
            n1,n2,c = s.popleft()
            if n1 and n2:
                m=max(m,c)
                for i in range(10):
                    s.append((n1.ch[i],n2.ch[i],c+1))
        return m
                    

