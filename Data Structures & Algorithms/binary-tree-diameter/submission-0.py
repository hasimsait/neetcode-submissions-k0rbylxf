# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.gMax=0
        def d(node):
            if node is None:
                return 0
            else:
                l=d(node.left)
                r=d(node.right)
                self.gMax = max( self.gMax , l+r)
                return max(l,r)+1
        
        d(root)
        return self.gMax
        