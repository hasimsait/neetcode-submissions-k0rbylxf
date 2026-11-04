class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        l={0:-1}
        c,m=0,float('inf')
        s=sum(nums)%p
        if s==0:
            return 0
        for i,n in enumerate(nums):
            c=(c+n)%p
            if (c-s+p)%p in l:
                m=min(m,i-l[(c-s+p)%p])
            l[c]=i
        return -1 if m>=len(nums) else m