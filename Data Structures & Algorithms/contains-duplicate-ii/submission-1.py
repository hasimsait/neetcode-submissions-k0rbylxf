class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        wind = [-1000000001 for x in range(k)]
        for x in nums:
            if x in wind:
                return True
            wind.append(x)
            wind = wind[1:]
        return False