class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a={x for x in range(1,len(nums)+1)}
        for n in nums:
            if n in a:
                a.remove(n)
        return list(a)

