class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ct=defaultdict(int)
        for n in nums:
            ct[n]+=1
        for n in ct:
            if ct[n]%2!=0:
                return False
        return True