class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==1 and nums[0]==1:
            return 2
        self.stack=[]
        def d(i):
            if nums[i]>0 and nums[i]<=len(nums):
                if nums[nums[i]-1]>0:
                    self.stack.append(nums[nums[i]-1])
                nums[nums[i]-1]=-999
        def s():
            if len(self.stack)>0:
                a=self.stack[0]
                self.stack=self.stack[1:]
                if a<=len(nums) and nums[a-1]>0 and nums[a-1]!= a and nums[a-1]<=len(nums):
                    self.stack.append(nums[a-1])
                if a<=len(nums) and a>0:
                    nums[a-1]=-999
        for i in range(len(nums)):
            d(i)
        while len(self.stack)!=0:
            s()
        for i,n in enumerate(nums):
            if n!=-999:
                return i+1
        return len(nums)+1
