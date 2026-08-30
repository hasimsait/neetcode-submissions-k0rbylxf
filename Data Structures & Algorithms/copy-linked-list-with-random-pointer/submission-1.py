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
        nodes={}
        t=Node(0)
        th=t
        headt=head
        while headt:
            t.next = Node(headt.val)
            nodes[headt]=t.next
            t=t.next
            headt=headt.next
        t.next = None
        headt=head
        t=th
        while headt:
            t=t.next
            if headt.random:
                t.random = nodes[headt.random]
            else:
                t.random = None
            headt=headt.next
        return th.next
