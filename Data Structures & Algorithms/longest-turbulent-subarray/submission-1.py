class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #could do single pass or rec w memo.
        def s(inc):
            i,j,lenmax,pv=0,1,1,arr[0]
            while i<len(arr) and j<len(arr):
                if (inc and arr[j]>pv) or (not inc and arr[j]<pv):
                    pv = arr[j]
                    j+=1
                    lenmax = max(lenmax,j-i)
                else:
                    i=j
                    j+=1
                    pv = arr[i]
                inc = not inc
            return lenmax
        return max(s(True),s(False))