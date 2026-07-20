class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        a=[0]*100001
        for n in nums:
            a[n+50000]+=1
        r=[]
        for i in range(100001):
            r+=[i-50000]*a[i]
        return r