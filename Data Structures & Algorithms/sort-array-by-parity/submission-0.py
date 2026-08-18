class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,ctr=0,0
        while ctr<len(nums): 
            t=nums[i]
            if t%2==1:
                nums.pop(i)
                nums.append(t)
                ctr+=1
            else:
                i+=1
                ctr+=1
        return nums