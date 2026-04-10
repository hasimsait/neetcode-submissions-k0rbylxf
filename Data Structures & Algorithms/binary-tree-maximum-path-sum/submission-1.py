# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.gmax = 0
        self.maxnode=root.val
        def d(node):
            if node is None:
                return 0
            else:
                self.maxnode = max(self.maxnode,node.val)
                l = max(0,d(node.left))
                r= max(0,d(node.right))
                self.gmax = max(self.gmax,l+r+node.val)
                return max(l,r)+node.val
        d(root)
        return self.gmax if self.gmax!=0 else self.maxnode