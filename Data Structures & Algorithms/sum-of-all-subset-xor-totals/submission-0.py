class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.gs=0
        def xor(s):
            if len(s)==0:
                return 0
            a= s[0]
            for c in s[1:]:
                a=a^c
            return a

        def c(i,last):
            self.gs+=xor(i)
            if last == len(nums):
                return
            for x in range(last,len(nums)):
                i.append(nums[x])
                c(i,x+1)
                i.pop()
            return
        c([],0)
        return self.gs