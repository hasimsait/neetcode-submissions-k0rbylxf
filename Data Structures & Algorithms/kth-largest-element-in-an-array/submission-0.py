class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a=[-2000 for a in range(k)]
        for i in nums:
            a.append(i)
            print(a)
            a.sort()
            a=a[1:]
        return a[0]
        