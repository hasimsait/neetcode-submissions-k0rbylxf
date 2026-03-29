class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset = []
        def d(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            d(i+1)
            subset.pop()
            d(i+1)
        d(0)
        return res
