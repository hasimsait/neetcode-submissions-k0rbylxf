class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c={}
        for i,n in enumerate(nums):
            c[str(n)]=i
        for i,n in enumerate(nums):
            if str(target-n ) in c and c[str(target-n)]!=i:
                return [i,c[str(target-n)]]