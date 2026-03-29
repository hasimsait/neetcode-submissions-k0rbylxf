# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def s(r,p):
            if r is None:
                return 0
            else:
                z=0
                if p<=r.val:
                    z=1
                pc=max(p,r.val)
                l=s(r.left,pc)
                a=s(r.right,pc)
                return z+l+a
        return s(root,root.val)
            

        