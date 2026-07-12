# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def dfs(self,n):
        if n is None:
            self.res.append("N")
            return
        self.res.append(str(n.val))
        self.dfs(n.left)
        self.dfs(n.right)
    def d(self,vals):
        if vals[self.i]=="N":
            self.i+=1
            return None
        node = TreeNode(int(vals[self.i]))
        self.i+=1
        node.left = self.d(vals)
        node.right = self.d(vals)
        return node
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []
        self.dfs(root)
        return ",".join(self.res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        v=data.split(",")
        self.i=0
        return self.d(v)
        

