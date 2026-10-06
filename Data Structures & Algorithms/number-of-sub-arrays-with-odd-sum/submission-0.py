class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ct=[1,0]
        p,r=0,0
        M=10**9+7
        for n in arr:
            p=(p+n)%2
            r=(r+ct[1-p])%M
            ct[p]+=1
        return r