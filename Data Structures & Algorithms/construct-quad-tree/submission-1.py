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
        def c(i1,i2,j1,j2):
            if i2<=i1 or j2<=j1 or i2>len(grid) or j2>len(grid):
                return None
            elif i2 == i1+1 and j2 == j1+1:
                return Node(grid[i1][j1],True,None,None,None,None)
            else:
                mi = (i2-i1)//2 + i1
                mj = (j2-j1)//2 + j1
                tl = c(i1,mi,j1,mj)
                tr = c(i1,mi,mj,j2)
                bl = c(mi,i2,j1,mj)
                br = c(mi,i2,mj,j2)
                allLeaf  = True
                for n in [tl,tr,bl,br]:
                    allLeaf = allLeaf and n.isLeaf
                if allLeaf and tl.val==tr.val and bl.val == br.val and br.val == tl.val:
                    #merge
                    return Node(tl.val,True,None,None,None,None)
                return Node(0,False,tl,tr,bl,br)
        return c(0,len(grid),0,len(grid[0]))