class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        l,r,c=0,len(people)-1,0
        while l<=r:
            if people[l]+people[r]<=limit:
                r-=1
            l+=1
            c+=1
        return c