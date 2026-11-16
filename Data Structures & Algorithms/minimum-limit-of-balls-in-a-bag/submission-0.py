class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l,r= 1,max(nums)
        n=r
        while l<=r:
            m=(l+r)>>1
            c=0
            for i in nums:
                c+=(i-1)//m
                if c>maxOperations:
                    break
            if c>maxOperations:
                l=m+1
            else:
                n=m
                r=m-1
        return n
