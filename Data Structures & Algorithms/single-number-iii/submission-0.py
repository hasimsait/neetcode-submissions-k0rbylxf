class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        axorb=0
        for n in nums:
            axorb = n ^ axorb
        a,b=0,0
        rmb = 1
        while rmb&axorb==0:
            rmb<<=1
        for n in nums:
            if rmb&n:
                a=a^n
            else:
                b=b^n
        return [a,b]
