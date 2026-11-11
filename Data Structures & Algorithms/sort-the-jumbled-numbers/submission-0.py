class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        x=[]
        for i,n in enumerate(nums):
            if n==0:
                x.append((mapping[n],i))
                continue
            s=c=0
            while n>0:
                s+=mapping[n%10]*10**c
                c+=1
                n=n//10
            x.append((s,i))
        x.sort()
        return [nums[b] for a,b in x]
