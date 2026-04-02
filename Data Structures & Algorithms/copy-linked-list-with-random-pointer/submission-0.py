"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None:None}
        h=head
        while h is not None:
            copy = Node(h.val)
            nodes[h]=copy
            h = h.next
        h=head
        while h is not None:
            copy = nodes[h]
            copy.next = nodes[h.next]
            copy.random = nodes[h.random]
            h=h.next
        return nodes[head]