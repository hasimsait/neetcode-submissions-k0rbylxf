# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def a(root):
            if (root.val<val and root.right is None):
                root.right = TreeNode(val=val)
                return root.right
            elif (root.val>val and root.left is None):
                root.left = TreeNode(val=val)
                return root.left
            elif root.val>val:
                return a(root.left)
            else:
                return a(root.right)
        if root is None:
            return TreeNode(val=val)
        a(root)
        return root

            
        