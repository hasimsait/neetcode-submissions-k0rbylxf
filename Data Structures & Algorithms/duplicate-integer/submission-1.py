class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for n in nums:
            if n in a:
                return True
            else:
                a.add(n)
        return False