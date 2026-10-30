class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a=[]
        ctr=0
        for n in nums:
            if n>pivot:
                a.append(n)
            elif n ==pivot:
                ctr+=1
        c=p=0
        while c<len(nums):
            if nums[c]<pivot:
                nums[p]=nums[c]
                p+=1
                c+=1
            else:
                c+=1
        for _ in range(ctr):
            nums[p]=pivot
            p+=1
        for x in a:
            nums[p]=x
            p+=1
        return nums
