class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i=0
        pre,post=[0],[0]
        for i in range(len(nums)):
            pre.append(pre[-1]+nums[i])
            post.append(post[-1]+nums[-i-1])
        for i in range(1,len(nums)+1):
            if pre[i]==post[-i]:
                return i-1
        return -1