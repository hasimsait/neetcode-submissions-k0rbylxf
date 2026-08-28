# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def d(node,prev):
            if node is None:
                return prev
            t=node.next
            node.next = prev
            return d(t,node)
        return d(head,None)
