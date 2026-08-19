class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s=sum(nums)
        ts=s//k
        nums.sort()
        nums=nums[::-1]
        if s%k!=0 or nums[0]>ts:
            return False
        u = [False]*len(nums)
        def s(c,k,csum):
            if k==0:
                return True
            if csum==ts:
                return s(0,k-1,0)
            for i in range(c,len(nums)):
                if not u[i] and csum+nums[i]<=ts:
                    u[i]=True
                    if s(i+1,k,csum+nums[i]):
                        return True
                    u[i]=False
                    if not csum: #prev sets used 5,1,1 when there is 4 and 2 unused
                        return False
            return False
        return s(0,k,0)
        