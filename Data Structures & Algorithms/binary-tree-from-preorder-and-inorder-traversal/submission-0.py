# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.p=self.i=0
        def dfs(l):
            if self.p>= len(preorder):
                return None
            if inorder[self.i]==l:
                self.i+=1
                return None
            root = TreeNode(preorder[self.p])
            self.p+=1
            root.left = dfs(root.val)
            root.right = dfs(l)
            return root
        return dfs(2000)