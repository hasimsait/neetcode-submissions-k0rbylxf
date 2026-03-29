# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def v(r,s):
            if r is None and s is None:
                return True
            elif r is None or s is None:
                return False
            elif r.val ==s.val:
                #both nodes exist, verify l,r
                return v(r.left,s.left) and v(r.right,s.right)
            else:
                return False
        posRoot = []
        def s(r,n):
            if r is None or s is None:
                return None
            else:
                if r.val==n.val:
                    posRoot.append(r)
                s(r.left,n)
                s(r.right,n)

        s(root,subRoot)
        for p in posRoot:
            if v(p,subRoot):
                return True
        return False

        