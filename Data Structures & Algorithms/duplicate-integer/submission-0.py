class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n={}
        for nu in nums:
            if nu not in n:
                n[nu]=1
            else: return True
        return False