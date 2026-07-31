class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a={x for x in nums1}
        b={x for x in nums2}
        for i in nums2:
            if i in a:
                a.remove(i)
        for i in nums1:
            if i in b:
                b.remove(i)
        return [list(a),list(b)]