class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        a = {}
        l_far,l_near,ans = 0,0,0

        for r, x in enumerate(nums):
            if x not in a:
                a[x]=0
            a[x] += 1

            if len(a) > k:
                del a[nums[l_near]]
                l_near += 1
                l_far = l_near

            if len(a) == k:
                while a[nums[l_near]] > 1:
                    a[nums[l_near]] -= 1
                    l_near += 1
                ans += l_near - l_far + 1

        return ans