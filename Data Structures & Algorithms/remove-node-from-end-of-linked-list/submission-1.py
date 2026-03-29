# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def amiend(node):
            if node is None:
                return 0
            a= amiend(node.next)+1
            if a==n+1:
                if node.next is not None:
                    node.next = node.next.next
            return a
            #n=2=> 4.next->0 4->1 3->2==n
        if head is None:
            return None
        if amiend(head)==n:
            return head.next
        return head        