class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)*2):
            a.append(nums[i%len(nums)])
        return a