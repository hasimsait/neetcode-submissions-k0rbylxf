class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: 
        r,c=0,0
        p=defaultdict(int)
        p[0]=1
        for i in nums:
            c+=i
            d=c-k
            if d in p:
                r+=p[d]
            p[c]+=1
        return r