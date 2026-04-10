class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m=[]
        res=[]
        for i in range(k-1):
            heapq.heappush(m,(-1*nums[i],i))
        for i in range(k-1,len(nums)):
            heapq.heappush(m,(-1*nums[i],i))
            b=heapq.heappop(m)
            while i-k>=b[1]:
                b=heapq.heappop(m)
            res.append(b[0]*-1)
            if b[1]!=i-k:
                heapq.heappush(m,b)
        return res
