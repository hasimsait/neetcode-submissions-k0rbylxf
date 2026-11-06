class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        r=sum(nums)
        l=0
        res=[]
        for i,n in enumerate(nums):
            res.append(n*i-l+r-n*(len(nums)-i))
            l+=n
            r-=n
        return res