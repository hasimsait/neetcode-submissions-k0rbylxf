# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def s(root,c):
            if not root:
                return False
            c+=root.val
            if not root.left and not root.right:
                return c ==targetSum
            return s(root.left,c) or s(root.right,c) 
        return s(root,0)