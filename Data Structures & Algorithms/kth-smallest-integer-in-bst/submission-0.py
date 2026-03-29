# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def s(r):
            if r is None:
                return []
            return s(r.left)+[r]+s(r.right)
        return s(root)[k-1].val