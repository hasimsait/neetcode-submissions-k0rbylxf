# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val==val:
            head=head.next
        if not head:
            return None
        t=head #head is the first linked list node that will stay
        while t.next:
            if t.next.val==val:
                t.next=t.next.next
            else:
                t=t.next
        return head
