class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        diffmin = 300000
        for i in range(k-1,len(nums)):
            diffmin=min(diffmin,nums[i]-nums[i-k+1])
        return diffmin