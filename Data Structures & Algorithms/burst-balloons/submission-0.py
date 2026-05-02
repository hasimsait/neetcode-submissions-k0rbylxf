class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        mem = {}
        def d(l,r):
            if l>r:
                return 0
            if (l,r) in mem:
                return mem[(l,r)]
            mem[(l,r)]=0
            for i in range (l,r+1):
                c=nums[l-1] * nums[i] * nums[r+1]
                c+=d(l,i-1)+d(i+1,r)
                mem[(l,r)]=max(mem[(l,r)],c)
            return mem[(l,r)]
        return d(1,len(nums)-2)