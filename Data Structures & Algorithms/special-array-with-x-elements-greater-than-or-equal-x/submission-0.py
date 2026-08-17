class Solution:
    def specialArray(self, nums: List[int]) -> int:
        c=defaultdict(int)
        for n in nums:
            c[n]+=1
        tr=0
        for i in range(1,max(nums)+1)[::-1]:
            tr+=c[i]
            if i==tr:
                return tr
        return -1
