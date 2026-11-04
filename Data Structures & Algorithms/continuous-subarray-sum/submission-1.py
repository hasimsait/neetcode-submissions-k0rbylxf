class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        l=set()
        l.add(0)
        p=0
        s=0
        for i, n in enumerate(nums):
            s=(s+n)%k
            if s in l:
                if p!=s:
                    return True
                else:
                    p=-1
            else:
                p=s
                l.add(s)
        return False
        