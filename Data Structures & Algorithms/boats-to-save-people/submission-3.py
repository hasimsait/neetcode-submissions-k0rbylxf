class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        people=people[::-1]
        i,j,boats=0,len(people)-1,0
        while i<=j:
            boats+=1
            if j>=i and people[j]+people[i]<=limit:
                j-=1
            i+=1
        return boats
