class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        s=sum(nums)
        dif = int(s-((len(nums)+1)*len(nums)/2))
        ptr = 0
        while nums[ptr]==ptr+1:
            ptr+=1
        if nums[ptr]==ptr:
            #duplicate 12344... some larger number will be missing
            return [ptr,ptr-dif]
        if nums[ptr]==ptr+2:
            #missing 1245 some larger number will have a duplicate
            return [ptr+1+dif,ptr+1]
        return -1