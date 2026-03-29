# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def s(n:TreeNode):
            if n is None:
                return []
            elif n.val==p.val:
                return [n]
            elif n.val==q.val:
                return [n]
            else:
                a=s(n.left)
                b=s(n.right)
                if len(a)==1 and len(b)==1:
                    return [n]
                else:
                    return a+b
        return s(root)[0]
        