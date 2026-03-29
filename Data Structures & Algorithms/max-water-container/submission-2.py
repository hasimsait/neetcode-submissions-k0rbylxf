class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        #memo={}
        def d(a,b):
            print(a,b)
            if a==b or a<0:
                return 0
            #if (a,b) in memo:
            #    return memo[(a,b)]
            s = min(heights[a],heights[b]) * abs(b-a)
            if heights[b]<heights[a]:
                s = max(s,d(a,b-1))
            else:
                s = max(s,d(a+1,b))
            #memo[(a,b)] = s
            return s#memo[(a,b)]
        return d(i,j)