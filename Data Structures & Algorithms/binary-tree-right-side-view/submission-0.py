# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodesByLevel = []
        def  d(node,level):
            if node is None:
                return
            else:
                while level>=len(nodesByLevel):
                    nodesByLevel.append([])
                nodesByLevel[level] = [node.val]+nodesByLevel[level]
                d(node.left,level+1)
                d(node.right,level+1)
        d(root,0)
        return [x[0] for x in nodesByLevel]
