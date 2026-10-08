class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        s={0:1}
        r=c=0
        for n in nums:
            c+=n
            r+=s[c-goal] if c-goal in s else 0
            if c not in s:
                s[c]=0
            s[c]+=1
        return r
