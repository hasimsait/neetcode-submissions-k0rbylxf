class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        s=sum(nums)
        x=[-a for a in nums]
        heapq.heapify(x)
        while len(x)>=3:
            t=-heapq.heappop(x)
            if t<s-t:
                return s
            s-=t
        return -1                

