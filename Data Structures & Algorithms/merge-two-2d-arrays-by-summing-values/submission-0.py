class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        s=[0]*1001
        for n,c in nums1:
            s[n]+=c
        for n,c in nums2:
            s[n]+=c
        r=[]
        for i in range(1001):
            if s[i]>0:
                r.append([i,s[i]])
        return r
