class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        last =[0,0]
        def replaceWithNum(i,sign):
            for j in range(i,len(nums)):
                if (nums[j]> 0 and sign==0) or (nums[j]<0 and sign==1):
                    last[sign]=j+1
                    last[1^sign]=i+1 
                    t=nums[j]
                    nums[j]=0
                    nums[:] = nums[:i]+[t]+nums[i:]
                    break
            return
        c=0
        p=0
        g=len(nums)
        while c<g:
            replaceWithNum(c,p)
            p=1^p
            c+=1
        return nums[:c]


