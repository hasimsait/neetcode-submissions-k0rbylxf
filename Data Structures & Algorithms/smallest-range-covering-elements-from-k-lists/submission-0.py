class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        import heapq
        a=[]
        m=float('-inf')
        res = float('inf')
        ans=[]
        for i,b in enumerate(nums):
            heapq.heappush(a,(b[0],i))
            m=max(m,b[0])
            nums[i].pop(0)
        while a:
            v,b=heapq.heappop(a)
            if m-v<res:
                ans = [v,m]
                res = m-v
            if len(nums[b])==0:
                return ans
            m=max(m,nums[b][0])
            heapq.heappush(a,(nums[b][0],b))
            nums[b].pop(0)
        return [-1,-1]

            

