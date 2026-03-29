class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i=-1
        for l,n in enumerate(arr):
            if n<=x:
                i=l
            elif n>x:
                break
        smaller = arr[:i+1] #(may include x)
        if i+1 == len(arr):
            return smaller[-k:]
        larger = arr[i+1:]
        smaller.reverse()
        ts,tl,t=-1,-1,0
        while t<k :
            if ts==len(smaller)-1 and  tl != len(larger)-1:
                tl=min(tl+k-t,len(larger)-1)
                t=k
            elif tl==len(larger)-1 and  ts!=len(smaller)-1:
                ts=min(ts+k-t,len(smaller)-1)
                t=k
            elif tl==len(larger)-1 and ts==len(smaller)-1:
                break
            else:
                if larger[tl+1]-x<x-smaller[ts+1]:
                    tl+=1
                else:
                    ts+=1
                t+=1
        a=smaller[:ts+1]
        return a[::-1]+larger[:tl+1]




