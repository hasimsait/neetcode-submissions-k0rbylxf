class Solution:
    def maxDifference(self, s: str) -> int:
        a=defaultdict(int)
        for c in s:
            a[c]+=1
        oddmax = 0
        evmin = len(s)
        for c in a:
            if a[c]%2==0:
                evmin = min(evmin,a[c])
            else:
                oddmax = max(oddmax,a[c])
        return oddmax-evmin