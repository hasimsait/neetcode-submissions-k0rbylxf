class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def getWhileConsec(n:List[int])->List[int]:
            i=1
            while i<len(n):
                if n[i]==n[i-1]+1:
                    i+=1
                else:
                    break
            return n[:i]

        a=list(set(nums))
        a.sort()
        #print(a)
        i=0
        m=0
        while i<len(a):
            c=getWhileConsec(a[i:])
            #print(c)
            m=max(m,len(c))
            i+=len(c)
        return m
        