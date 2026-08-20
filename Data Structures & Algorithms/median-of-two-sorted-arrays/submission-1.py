class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2
        
        while low <= high:
            i = (low + high) // 2
            j = half_len - i
            
            # Boundary values around the partitions (use infinity for out-of-bounds)
            max_left_a = float('-inf') if i == 0 else nums1[i - 1]
            min_right_a = float('inf') if i == m else nums1[i]
            
            max_left_b = float('-inf') if j == 0 else nums2[j - 1]
            min_right_b = float('inf') if j == n else nums2[j]
            
            # Valid partition found
            if max_left_a <= min_right_b and max_left_b <= min_right_a:
                if (m + n) % 2 == 1:
                    return float(max(max_left_a, max_left_b))
                return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2.0
            
            # Too far right in nums1; move left
            elif max_left_a > min_right_b:
                high = i - 1
            # Too far left in nums1; move right
            else:
                low = i + 1