class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c=defaultdict(int)
        for a in arr1:
            c[a]+=1
        r=[]
        for s in arr2:
            r += c[s]*[s]
            del c[s]
        l=[]
        for x in c:
            l += c[x]*[x]
        l.sort()
        return r+l
        