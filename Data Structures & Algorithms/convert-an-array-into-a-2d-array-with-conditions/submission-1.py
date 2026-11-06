class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        l=defaultdict(int)
        cmax = 0
        for n in nums:
            l[n]+=1
            cmax = max(cmax,l[n])
        l=defaultdict(int)
        a=[set() for _ in range(cmax+1)]
        for n in nums:
            a[l[n]].add(n)
            l[n]+=1
        return [list(x) for x in a[:-1]] #set iterator makes it stable 

