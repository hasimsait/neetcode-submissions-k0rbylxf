class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        m = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(m)
        for i in range(k):
            n, j = heapq.heappop(m)
            nums[j] *= multiplier
            heapq.heappush(m, (nums[j], j))

        return nums