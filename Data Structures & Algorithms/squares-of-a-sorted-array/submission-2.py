class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[0]*(max(max(nums),-min(nums))+1)
        for i in nums:
            a[abs(i)]+=1
        cursor = 0
        for i,x in enumerate(a):
            for j in range(x):
                nums[cursor]=i*i
                cursor+=1
        return nums