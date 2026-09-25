class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l,r,c=0,0,0
        while r<minutes:
            if grumpy[r]:
                c+=customers[r]
            r+=1
        a=c
        while r<len(customers):
            if grumpy[r]:
                c+=customers[r]
            if grumpy[l]:
                c-=customers[l]
            a=max(a,c)
            l+=1
            r+=1
        ans = 0
        for i,g in enumerate(grumpy):
            if not g:
                ans+=customers[i]
        return ans+a

        