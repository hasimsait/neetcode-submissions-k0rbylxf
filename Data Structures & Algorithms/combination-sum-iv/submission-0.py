class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        mem={0:1}
        def se(left):
            if left in mem:
                return mem[left]
            r=0
            for j in range(len(nums)):
                if nums[j]>left:
                    break
                r+=se(left - nums[j])
            mem[left]=r
            return r
        return se(target)