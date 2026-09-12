class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        ct=0
        ch=-1
        for n in nums:
            if ch!=n:
                ct-=1
                if ct<=0:
                    ch=n
                    ct=1
            else:
                ct+=1
        #cant get a split where dominant element of left and right is the same
        #and different than the  dominant element of nums
        ct=0
        for n in nums:
            if n==ch:
                ct+=1
        cc=0
        for i in range(len(nums)-1):
            if nums[i]==ch:
                cc+=1
            if 2*cc>i+1 and 2*(ct-cc)>len(nums)-i-1:
                return i
        return -1