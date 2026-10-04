class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l,r,s=0,k,0
        t=threshold*k
        for i in range(k):
            s+=arr[i]
        ans = 1 if s>=t else 0
        while r<len(arr):
            s+=arr[r]
            s-=arr[l]
            if s>=t:
                ans+=1
            r+=1
            l+=1
        return ans