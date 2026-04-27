class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cmax =-1
        for i in range(len(arr))[::-1]:
            t=max(cmax,arr[i])
            arr[i]=cmax
            cmax = t
        return arr