class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s=defaultdict(int)
        s[0]+=1
        p=r=0
        for n in nums:
            p=(p+n+k)%k
            r+=s[p]
            s[p]+=1
        return r