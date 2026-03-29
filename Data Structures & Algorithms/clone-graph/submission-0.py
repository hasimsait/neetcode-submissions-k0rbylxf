"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeByOriginal = {}
        def clone(n,fromN):
            if n is None:
                None
            else:
                if n in nodeByOriginal:
                    return nodeByOriginal[n]
                else:
                    cn=Node(n.val)
                    nodeByOriginal[n]=cn
                    for neighbor in n.neighbors:
                        if neighbor!=fromN:
                            cnn = nodeByOriginal[neighbor] if neighbor in nodeByOriginal else clone(neighbor,n)
                            cn.neighbors.append(cnn)
                        else:
                            cn.neighbors.append(nodeByOriginal[fromN])
                    
                return cn
        return clone(node,None)
        