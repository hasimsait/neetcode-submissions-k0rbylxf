# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        s=deque()
        s.append((root.right,root.left))
        while s:
            cl,cr=s.popleft()
            if not cr and not cl:
                continue
            if not cr or not cl or cl.val!=cr.val:
                return False
            s.append((cl.left,cr.right))
            s.append((cr.left,cl.right))
        return True