class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        class Node:
            def __init__(self,val,n):
                self.val = val
                self.n = n
        h=None
        r=[0]*len(nums)
        for i in nums[::-1]:
            h=Node(i,h)
        t=h
        while t and t.n:
            if t.val == t.n.val:
                t.val*=2
                t.n=t.n.n
            t=t.n
        c=0
        while h:
            if h.val!=0:
                r[c]=h.val
                c+=1
            h=h.n
        return r


