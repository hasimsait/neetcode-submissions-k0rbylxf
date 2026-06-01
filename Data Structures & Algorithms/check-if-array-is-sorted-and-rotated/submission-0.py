class Solution:
    def check(self, nums: List[int]) -> bool:
        def checkSorted(a,b,lmin):
            print(a)
            while a:
                c=a.pop(0)
                if c<b or c>lmin:
                    return False
            return True
        prev  = nums[0]
        lmin  = nums[0]
        while nums:
            a = nums.pop(0)
            if a<prev:
                return checkSorted(nums,a,lmin)
            prev=a
        return True
            

