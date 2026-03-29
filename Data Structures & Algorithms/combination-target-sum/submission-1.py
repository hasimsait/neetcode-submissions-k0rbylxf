class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        def dfs(a,s):
            if s>target:
                return
            elif s==target:
                res.append([nums[x] for x in a])
            else:
                for b in range(a[-1],len(nums)):
                    x=nums[b]+s
                    a.append(b)
                    dfs(a,x)
                    a.pop()
        for i,x in enumerate(nums):
            dfs([i],x)

        return res            
