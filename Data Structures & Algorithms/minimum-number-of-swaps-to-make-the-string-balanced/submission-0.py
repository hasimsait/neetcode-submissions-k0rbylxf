class Solution:
    def minSwaps(self, s: str) -> int:
        r=0
        for c in s:
            if c=='[':
                r+=1
            elif r>0:
                r-=1
        return (r+1)//2