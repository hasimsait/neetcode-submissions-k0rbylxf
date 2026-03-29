class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x=[1]
        #[1,2,4,6]
        #[1,1,2,8,48]
        #multiplied everything to its left, now needs right

        for i,num in enumerate(nums):
            x.append(x[-1]*num) 
        i=len(nums)
        y=nums.append(1)
        z=[1]
        while(i>0):
            i-=1
            z.append(z[-1]*nums[i])
        res = []
        z=z[:-1]
        for i,r in enumerate(z[::-1]):
            res.append(r*x[i])

        #[   1, 1, 2, 8, 48]
        # 48 48 24 6  1
        #    48 24 12 8
        #[1,6,24,48]
        return res

        