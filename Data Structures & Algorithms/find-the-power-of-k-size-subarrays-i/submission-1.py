class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        r=[-1]*(len(nums)-k+1)
        p=nums[0]-1
        lv=0
        for i in range(k-1):
            if nums[i]!=p+1:
                lv=i
            p=nums[i]
        for i in range(k-1,len(nums)):
            if nums[i]!=p+1:
                lv=i
            if i-lv>=k-1:
                r[i-k+1]=nums[i]
            p=nums[i]
        return r


