class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=defaultdict(int)
        for x in nums:
            a[x]+=1
        r = 0
        for x in a:
            r+=a[x] * (a[x]-1)/2
        return int(r)
