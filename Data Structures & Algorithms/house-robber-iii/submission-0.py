# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        mem = {}
        def c(root):
            if root is None:
                return 0
            if root not in mem:
                p = root.val
                #skipleft right take cur
                if root.left is not None:
                    p+=c(root.left.left)+c(root.left.right)
                if root.right is not None:
                    p+=c(root.right.left)+c(root.right.right)
                #skip cur
                s=c(root.right)+c(root.left)
                mem[root] = max(s,p)
            return mem[root]
        return c(root)