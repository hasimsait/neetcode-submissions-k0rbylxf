class Solution:
    def minOperations(self, nums: List[int]) -> int:
        a=defaultdict(int)
        for n in nums:
            a[n]+=1
        s=0
        for n in a:
            if a[n]%2==1 and a[n]<3:
                return -1
            if a[n]%2==1:
                s+=1
                a[n]-=3
            s+=(a[n]//6)*2
            a[n]-=(a[n]//6)*6
            s+=a[n]//2
        return s