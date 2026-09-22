class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total=sum(nums)
        extra = total%p
        if extra==0:
            return 0
        r={0:-1}
        c=0
        self.r=len(nums)
        for i,n in enumerate(nums):
            c=(c+n)%p
            s=(c-extra+p)%p
            if s in r:
                l=i-r[s]
                self.r=min(self.r,l)
            r[c]=i
        return -1 if self.r==len(nums) else self.r