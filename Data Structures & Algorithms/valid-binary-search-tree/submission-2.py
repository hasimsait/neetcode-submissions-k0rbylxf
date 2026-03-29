# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root):
            rv=root.val
            #itself,min,max
            r=(rv,rv,rv,True)
            if root.right is None and root.left is None:
                #print(root.val)
                return r
            if root.right is None:
                l=valid(root.left)
                #print(root.val,l)
                if l[3]==False or l[0]>=rv or l[1]>=rv or l[2]>=rv:
                    return (0,0,0,False)
                else:
                    return (rv,l[1],rv,True)
            if root.left is None:
                r=valid(root.right)
                #print(root.val,r)
                if r[3]==False or r[0]<=rv or r[1]<=rv or r[2]<=rv:
                    return (0,0,0,False)
                else:
                    return (rv,rv,r[2],True)
            r=valid(root.right)
            if r[3]==False or r[0]<=rv or r[1]<=rv or r[2]<=rv:
                #print(root.val,r)
                return (0,0,0,False)
            l=valid(root.left)
            if l[3]==False or l[0]>=rv or l[1]>=rv or l[2]>=rv:
                #print(root.val,l)
                return (0,0,0,False)
            else:
                return (rv,l[1],r[2],True)
        if root is None:
            return True
        return valid(root)[3]