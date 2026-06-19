# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.c=0
        def s(node):
            if node is None:
                return
            s(node.left)
            s(node.right)
            if not(node.val<low or node.val>high):
                self.c+=node.val
            return
        s(root)
        return self.c