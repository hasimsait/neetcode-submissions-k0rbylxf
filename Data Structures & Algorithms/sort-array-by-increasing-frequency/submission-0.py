class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        a=defaultdict(int)
        for n in nums:
            a[n]+=1
        l=[(a[n],-n) for n in a]
        l.sort()
        r=[]
        for x in l:
            for i in range(x[0]):
                r.append(-x[1])
        return r