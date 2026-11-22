# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def c(root,cv):
            if not root:
                return 0
            if root and not (root.left or root.right):
                return cv*10+root.val
            return c(root.right, cv*10+root.val) + c(root.left, cv*10+root.val)
        return c(root,0)