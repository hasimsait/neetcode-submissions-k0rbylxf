# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=[[root,0]]
        l={}
        while len(q)>0:
            a=q[0]
            q=q[1:]
            node,level = a[0],a[1]
            if node.left is not None:
                q.append([node.left,level+1])
            if node.right is not None:
                q.append([node.right,level+1])
            if level not in l:
                l[level]=[]
            l[level].append(node.val)

        res = [l[level] for level in l]
        return res
