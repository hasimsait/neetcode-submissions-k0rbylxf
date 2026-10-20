class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        f={0:-1}
        r,c=0,0
        for i,x in enumerate(nums):
            if x:
                c+=1
            else:
                c-=1
            if c in f:
                #if the csum was -1 at index 3 and is -1 now, (3,i] is valid
                #we dont update the dict. we want the earliest occurence to maximize length
                r=max(r,i-f[c])
            else:
                f[c]=i
        return r

