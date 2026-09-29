class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        class Node:
            def __init__(self,cs,ce):
                self.cs=cs
                self.ce=ce
                self.w=0
                self.children = {}
            def add_child(self,cs,ce):
                self.w+=1
                if (cs,ce) not in self.children:
                    self.children[(cs,ce)]=Node(cs,ce)
                return self.children[(cs,ce)]
        root = Node(' ',' ')
        r=0
        for w in words[::-1]:
            t=root
            for i in range(len(w)):
                t=t.add_child(w[i],w[-i-1])
            t.add_child(' ',' ')
            r+=t.w -1
        return r            


