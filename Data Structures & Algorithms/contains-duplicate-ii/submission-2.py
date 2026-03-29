class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        wind = set()
        for i,x in enumerate(nums):
            if x in wind:
                return True
            
            wind.add(x)
            if len(wind)>k:
                wind.remove(nums[i-k])
        return False