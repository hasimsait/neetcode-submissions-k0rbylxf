class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l,r=max(nums),sum(nums)
        for i in range(1,n):
            nums[i]+=nums[i-1]
        nums[:]=[0]+nums
        def splitable(maxs):
            s=0
            i=0
            while i<n:
                l,r=i+1,n
                while l<=r:
                    m = (l + r)//2
                    if nums[m]-nums[i]<=maxs:
                        l=m+1
                    else:
                        r=m-1
                s+=1
                i=r
                if s>k:
                    return False
            return True
        res = r
        while l<=r:
            m=(l+r)//2
            if splitable(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res

