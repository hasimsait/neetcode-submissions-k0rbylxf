class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        a=[0]*100001
        for n in nums:
            a[n+50000]+=1
        c=0
        r=[-50001]*len(nums)
        for i in range(100001):
            for x in range(c,c+a[i]):
                r[x]=i-50000
            c+=a[i]
        return r