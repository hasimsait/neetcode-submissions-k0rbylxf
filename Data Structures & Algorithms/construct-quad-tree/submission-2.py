"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def construct(i1,i2,j1,j2):
            if i1==i2 or j1==j2:
                return None
            iv = grid[i1][j1]
            leaf =True
            for i in range(i1,i2):
                for j in range(j1,j2):
                    if grid[i][j]!=iv:
                        leaf=False
                        break
            if leaf:
                return Node(iv, leaf, None, None, None, None)
            im=(i2-i1)//2+i1
            jm=(j2-j1)//2+j1
            return Node(iv,leaf,construct(i1,im,j1,jm),construct(i1,im,jm,j2),construct(im,i2,j1,jm),construct(im,i2,jm,j2))
        return construct(0,len(grid),0,len(grid[0]))