class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[0]*10001
        for i in nums:
            a[abs(i)]+=1
        r=[]
        for i,x in enumerate(a):
            for j in range(x):
                r.append(i*i)
        return r