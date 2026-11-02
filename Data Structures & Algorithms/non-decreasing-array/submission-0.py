class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        decreased = False
        nums.append(float('inf'))
        p=float('-inf')
        for i,e in enumerate(nums):
            if e<p:
                if decreased:
                    return False
                if i <= 1 or e >= nums[i - 2]:
                    p = e
                decreased=True
            else:
                p=e
        return True                
