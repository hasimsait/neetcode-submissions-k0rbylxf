# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def i(root):
            if root is None:
                return []
            else:
                return i(root.left) + [root.val] + i(root.right)
        return i(root)